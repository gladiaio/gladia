from importlib_metadata import version
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="resnext101_64x4d",
        weights="resnext101_64x4d_quantized_fbgemm_v1",
        weights_version="IMAGENET1K_FBGEMM_V1",
        quantized=True,
    )
    output = model(img, top_k)

    return output
