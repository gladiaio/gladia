from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="shufflenet_v2_x2_0", weights="ShuffleNet_V2_X2_0_Weights"
    )
    output = model(img, top_k)

    return output
