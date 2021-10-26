import numpy as np
import cv2
import pytesseract
from PIL import Image
from icecream import ic
import re

def predict(image, source_language):
    nparr = np.fromstring(image, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR) 
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    gray_thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    text = pytesseract.image_to_string(gray_thresh)
    out = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text)
    return [out.strip()]