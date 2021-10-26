import easyocr

import os
import re
from icecream import ic

def predict(image, source_language):

    reader = easyocr.Reader([source_language], gpu = True)
    text = reader.readtext(image, detail = 0)
    
    return text