import io

import cv2
import face_recognition
import numpy as np
from unifai_api_utils.image_management import blur_image
from unifai_api_utils.io import _open
from unifai_api_utils.options import get_option
from unifai_api_utils.citation import get_doi
from icecream import ic
from skimage.filters import gaussian
from unifai_api_utils.file_management import input_to_files
from PIL import Image
@input_to_files
def predict(image):
    sigma = 50
    print(image)

    image = face_recognition.load_image_file(image)

    locations = face_recognition.face_locations(image)
    
    image = io.imread(image)
    for location in locations:
        startY = location[0]
        endY = location[2]
        startX = location[1]
        endX = location[3]
        image = blur_image(image, startX, endX, startY, endY, sigma=sigma)

    res, im_png = cv2.imencode(".png", image)

    return im_png


def details():
    details = {
        "doi": "10.1371/journal.pone.0029740",
        "example_figure": "https://camo.githubusercontent.com/5eb8b4f1f63dbdbb5c30afb10575d6ebe24bb0a156e6b81296c8191183f33edf/68747470733a2f2f692e6962622e636f2f3559304d3258622f6578616d706c652e706e67",
        "description": "Image Uncolorization will vintage your picture to turn them into black and white style.",
    }
    details += get_doi(details["doi"])
    return details
