import io
import cv2
import numpy as np


def predict(image):
    nparr = np.fromstring(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res, im_png = cv2.imencode(".png", gray_image)

    return im_png


def details():
    details = {
        "doi": "10.1371/journal.pone.0029740",
        "example_figure": "https://camo.githubusercontent.com/5eb8b4f1f63dbdbb5c30afb10575d6ebe24bb0a156e6b81296c8191183f33edf/68747470733a2f2f692e6962622e636f2f3559304d3258622f6578616d706c652e706e67",
        "description": "Image Uncolorization will vintage your picture to turn them into black and white style.",
    }
    details += get_doi(details["doi"])
    return details


def get_doi(doi):
    crossref_url = f"http://api.crossref.org/works/{doi}"
    req = requests.get(crossref_url)
    return req.content
