from importlib_metadata import version
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="resnext101_32x8d",
        weights="ResNeXt101_32X8D_QuantizedWeights",
        weights_version="IMAGENET1K_FBGEMM_V2",
        quantized=True
    )
    output = model(img, top_k)

    return output
