import re

import cv2
import numpy as np
from gladia_api_utils.io import _open


def predict(image: bytes, source_language: str) -> [str]:
    """
    Call the tesseract ocr, apply a median blurring filter to the input image and return the text detected in the image

    :param image: image to provide to the ocr
    :param source_language: [UNUSED] language of the text to be searched
    :return: characters found in the image
    """

    import pytesseract

    del source_language

    image = _open(image)

    np_image = np.array(image)

    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)

    gray_thresh = cv2.medianBlur(gray_image, 3)

    text = str(pytesseract.image_to_string(gray_thresh))

    out = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]", "", text)

    return [out.strip()]
