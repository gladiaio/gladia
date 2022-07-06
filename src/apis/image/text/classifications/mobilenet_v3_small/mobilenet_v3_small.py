from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="mobilenet_v3_small", weights="MobileNet_V3_Small_Weights"
    )
    output = model(img, top_k)

    return output
