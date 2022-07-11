from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="mobilenet_v3_large",
        weights="MobileNet_V3_Large_QuantizedWeights",
        weights_version="IMAGENET1K_QNNPACK_V1",
        quantized=True,
    )
    output = model(img, top_k)

    return output
