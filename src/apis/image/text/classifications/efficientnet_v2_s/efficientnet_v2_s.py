from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="efficientnet_v2_s", weights="EfficientNet_V2_S_Weights"
    )
    output = model(img, top_k)

    return output
