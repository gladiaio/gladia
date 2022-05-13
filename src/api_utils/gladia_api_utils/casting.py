import io
import os
import pathlib
import string

import numpy as np
import PIL
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from icecream import ic
from starlette.responses import StreamingResponse

from .file_management import get_file_type
import json
import errno

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)



def cast_response(response, expected_output: dict):

    if isinstance(response, PIL.Image.Image):
        ic("converting to pil")
        ioresult = io.BytesIO()
        response.save(ioresult, format="png")
        ioresult.seek(0)
        return StreamingResponse(ioresult, media_type="image/png")

    elif isinstance(response, np.ndarray):
        if expected_output["type"] == "image":
            ic("converting to image from numpy")
            ioresult = io.BytesIO(response.tobytes())
            ioresult.seek(0)
            return StreamingResponse(ioresult, media_type="image/png")
        elif expected_output["type"] == "text":
            ic("converting to json from numpy")
            return JSONResponse(content=jsonable_encoder(response.tolist()))

    elif isinstance(response, bytes):
        ioresult = io.BytesIO(response)
        ioresult.seek(0)
        if expected_output["type"] == "image":
            ic("converting to image from bytes")
            return StreamingResponse(ioresult, media_type="image/png")

    elif isinstance(response, io.IOBase):
        ioresult = response
        ioresult.seek(0)
        if expected_output["type"] == "image":
            ic("converting to image from io")
            return StreamingResponse(ioresult, media_type="image/png")

    elif isinstance(response, list):
        ic("converting to json from list")

        return json.dumps(response, cls=NpEncoder, ensure_ascii=False).encode('utf8')

    elif isinstance(response, str):
        ic(f"converting string output")
        try:
            if pathlib.Path(response).is_file():
                ic("streaming file", response)
                file_to_stream = open(response, "rb")
                out = StreamingResponse(file_to_stream, media_type=get_file_type(response))
                os.remove(response)
                ic(f"returning file {response}")
                return out
            else:
                ic(f"returning string {response}")
                return response
        except OSError as oserr:
            if oserr.errno != errno.ENAMETOOLONG:
                return response
            else:
                return response
        
    elif isinstance(response, bool):
        ic(f"converting boolean")
        return response
    elif isinstance(response, float):
        ic(f"converting float")
        return response
    else:
        ic(f"converting whatever")
        ioresult = response
        ioresult.seek(0)
        return StreamingResponse(ioresult, media_type="image/png")
