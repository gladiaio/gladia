from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="squeezenet1_0", weights="SqueezeNet1_0_Weights"
    )
    output = model(img, top_k)

    return output
