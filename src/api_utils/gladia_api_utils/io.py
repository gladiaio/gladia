import io
from logging import raiseExceptions
from typing import Any

import magic
import numpy as np
import pandas as pd
from icecream import ic
from PIL import Image
import cv2
from .file_management import get_buffer_category, get_buffer_type, get_mime_category
from pathlib import Path


def _open(input, btype=None, options=dict()) -> Any:
    """
    convert input to infer, numpy, PIL image, binary, pdf,
    """

    output = None

    if isinstance(input, io.BytesIO):
        ic("Converting io.BytesIO to bytes object")
        buffer = input.read()
    elif isinstance(input, str):
        if Path(input).is_file():
            with open(input, "rb") as fh:
                buffer = io.BytesIO(fh.read())
                buffer = buffer.getvalue()
        else:
            buffer = input
    else:
        buffer = input

    if btype in ["numpy", "pil"]:
        if get_buffer_category(buffer) == "image":
            ic("pil/numpy-image")
            output = cv2.imdecode(np.fromstring(buffer, np.uint8), cv2.IMREAD_COLOR)
        else:
            ic("pil/numpy-else")
            output = globals()[f"to_{btype}"](buffer)

    else:
        ic("infere type")
        btype = get_buffer_category(buffer)
        if btype == "image":
            ic("infere type image")
            output = to_pil(buffer)
        elif btype == "flat_structured_data":
            ic("infere type structured data")
            output = to_pandas(buffer)
        else:
            output = buffer

    return output


def to_numpy(buffer):
    return np.array(Image.open(io.BytesIO(buffer)))


def to_pil(buffer):
    data = to_numpy(buffer)
    return Image.fromarray(np.uint8(data))


def to_pandas(buffer):
    buffer_mime_type = get_buffer_type(buffer)
    get_buffer_category = get_mime_category(buffer_mime_type)
    output = None

    if buffer_mime_type == "text/csv":
        output = pd.read_csv(buffer)
    elif buffer_mime_type == "json":
        output = pd.read_json(buffer)
    elif get_buffer_category == "excel":
        output = pd.read_json(buffer)
    elif get_buffer_category == "web_content":
        output = pd.read_html(buffer)
    elif buffer_mime_type == "hdf5":
        raiseExceptions("Not implemented Yet")
    elif buffer_mime_type == "orc":
        raiseExceptions("Not implemented Yet")
    elif buffer_mime_type == "parquet":
        raiseExceptions("Not implemented Yet")
    elif buffer_mime_type == "sas":
        raiseExceptions("Not implemented Yet")
    elif buffer_mime_type == "spss":
        raiseExceptions("Not implemented Yet")
    elif buffer_mime_type == "spss":
        raiseExceptions("Not implemented Yet")
    elif buffer_mime_type == "pickle":
        raiseExceptions("Not implemented Yet")

    return output
