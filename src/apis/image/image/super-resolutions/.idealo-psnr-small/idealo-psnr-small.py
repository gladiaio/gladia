import tempfile

import numpy as np
from PIL import Image


def predict(image: str) -> str:
    """
    Apply super resolution on the provided image

    :param image: path to the input image
    :return: path to the output image
    """

    from ISR.models import RDN, RRDN

    # open image from path
    img = Image.open(image)

    model_gans = RRDN(weights="gans")
    output = tempfile.NamedTemporaryFile(suffix=".png", delete=False).name

    img = model_gans.predict(np.array(img))
    Image.fromarray(img).save(output)

    return output
