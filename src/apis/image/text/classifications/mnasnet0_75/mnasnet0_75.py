from gladia_api_utils.io import _open
from torchvision.io import read_image
from torchvision.models import Inception_V3_Weights, inception_v3


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    output = list()
    weights = Inception_V3_Weights.DEFAULT
    model = inception_v3(weights=weights)
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
