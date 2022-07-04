from gladia_api_utils import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="convnext_small", weights="ConvNeXt_Small_Weights"
    )
    output = model(img, top_k)

    return output
