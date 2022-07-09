from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="resnet50",
        weights="ResNet50_QuantizedWeights",
        weights_version="IMAGENET1K_FBGEMM_V1",
        quantized=True
    )
    output = model(img, top_k)

    return output
