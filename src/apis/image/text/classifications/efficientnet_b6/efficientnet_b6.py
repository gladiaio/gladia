from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="efficientnet_b6", weights="EfficientNet_B6_Weights"
    )
    output = model(img, top_k)

    return output
