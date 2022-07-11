from typing import Dict, List

from torch import topk as get_top_k
from torchvision import models as torchvision_models
from torchvision.io import read_image
from torchvision.models import quantization as torchvision_quantized_models


class TorchvisionModel:
    """Wrapping class for torchvision.models"""

    def __init__(
        self,
        model_name: str,
        weights: str,
        weights_version: str = "DEFAULT",
        quantized: bool = False,
    ) -> None:
        """Initialize the TorchvisionModel class

        Args:
            model_name (str): name of the model to load (must be the same named as in torchvision.models)
            weights (str): weights to load (must be the same named as in torchvision.models)
            weights_version (str, optional): version of the weights to load. Defaults to "DEFAULT".
        """
        if quantized:
            self.__weights = getattr(torchvision_quantized_models, weights)
        else:
            self.__weights = getattr(torchvision_models, weights)

        self.__weights = getattr(self.__weights, weights_version)

        if quantized:
            self.__model = getattr(torchvision_quantized_models, model_name)(
                weights=self.__weights, quantize=True
            )
        else:
            self.__model = getattr(torchvision_models, model_name)(
                weights=self.__weights
            )

        self.__model.eval()

        self.__preprocessing = self.__weights.transforms()

    def __call__(self, image, top_k: int = 1) -> List[Dict[str, int]]:
        """Apply the preprocessing associated with the loaded weights and apply the forward pass to the input value.

        Args:
            image (PIL.Image): Input value to preprocess and use in the forward pass
            top_k (int, optional): Number of classes to return. Defaults to 1.

        Returns:
            List[Dict[str, int]]: List of the predicted classes associated with it score
        """

        preprocessed_image = self.__preprocessing(image).unsqueeze(0)

        prediction = self.__model(preprocessed_image).squeeze(0).softmax(0)

        top_class_ids = get_top_k(prediction, int(top_k)).indices

        output = []
        for class_id in top_class_ids:
            output.append(
                {
                    "class": self.__weights.meta["categories"][class_id],
                    "score": prediction[class_id].item(),
                }
            )

        return output
