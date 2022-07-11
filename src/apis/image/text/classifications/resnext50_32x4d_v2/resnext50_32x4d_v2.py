from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from importlib_metadata import version


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="resnext50_32x4d",
        weights="ResNeXt50_32X4D_Weights",
        weights_version="IMAGENET1K_V2",
    )
    output = model(img, top_k)

    return output
