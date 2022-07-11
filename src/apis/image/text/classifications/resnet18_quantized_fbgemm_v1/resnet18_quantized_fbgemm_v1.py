from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="resnet18",
        weights="ResNet18_QuantizedWeights",
        weights_version="IMAGENET1K_FBGEMM_V1",
        quantized=True,
    )
    output = model(img, top_k)

    return output
