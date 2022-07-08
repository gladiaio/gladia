from importlib_metadata import version
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="regnet_y_3_2gf",
        weights="RegNet_Y_3_2GF_Weights",
        weights_version="IMAGENET1K_V2",
    )
    output = model(img, top_k)

    return output
