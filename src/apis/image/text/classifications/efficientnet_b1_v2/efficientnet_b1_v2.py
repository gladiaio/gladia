from torchvision.io import read_image
from torchvision.models import efficientnet_b1, EfficientNet_B1_Weights


from gladia_api_utils.io import _open


def predict(image: bytes, top_k: int = 1) -> [str]:
    img = _open(image)

    output = list()
    weights = EfficientNet_B1_Weights.IMAGENET1K_V2
    model = efficientnet_b1(weights=weights)
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

    del model
    del weights

    return output
