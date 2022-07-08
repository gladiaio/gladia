from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    model = TorchvisionModel(model_name="swin_t", weights="Swin_T_Weights")
    output = model(img, top_k)

    return output
