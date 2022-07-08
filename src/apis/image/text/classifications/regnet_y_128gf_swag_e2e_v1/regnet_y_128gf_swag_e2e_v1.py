from importlib_metadata import version
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="regnet_y_128gf",
        weights="RegNet_Y_128GF_Weights",
        weights_version="IMAGENET1K_SWAG_E2E_V1",
    )
    output = model(img, top_k)

    return output
