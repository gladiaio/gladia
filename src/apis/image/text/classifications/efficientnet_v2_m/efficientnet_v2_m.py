from torchvision.io import read_image
from torchvision.models import efficientnet_v2_m, EfficientNet_V2_M_Weights


from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    output = list()
    weights = EfficientNet_V2_M_Weights.DEFAULT
    model = efficientnet_v2_m(weights=weights)
    model.eval()

    # Step 2: Initialize the inference transforms
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0)

    # Step 4: Use the model and print the predicted category
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    output.append({"class": category_name, "score": score})
    return output
