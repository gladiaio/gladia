from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="regnet_x_400mf",
        weights="RegNet_X_400MF_Weights",
        weights_version="IMAGENET1K_V1",
    )
    output = model(img, top_k)

    return output
