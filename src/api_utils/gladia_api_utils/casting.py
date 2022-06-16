import io
import os
import PIL
import json
import pathlib
import numpy as np

from warnings import warn
from .file_management import get_file_type
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.responses import StreamingResponse


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


def __convert_pillow_image_response(response: PIL.Image.Image):
    ioresult = io.BytesIO()

    response.save(ioresult, format="png")
    ioresult.seek(0)

    return StreamingResponse(ioresult, media_type="image/png")


def __convert_ndarray_response(response: np.ndarray, output_type: str):
    if output_type == "image":
        ioresult = io.BytesIO(response.tobytes())
        ioresult.seek(0)

        return StreamingResponse(ioresult, media_type="image/png")

    elif output_type == "text":
        return JSONResponse(content=jsonable_encoder(response.tolist()))

    else:
        warn(f"response is numpy array but expected output type {output_type} which is not supported.")

        return response


def __convert_bytes_response(response: bytes, output_type: str):
    ioresult = io.BytesIO(response)
    ioresult.seek(0)

    if output_type == "image":
        return StreamingResponse(ioresult, media_type="image/png")

    else:
        warn(f"response is bytes but expected output type {output_type} which is not supported.")

    return response


def __convert_io_response(response: io.IOBase, output_type: str):
    response.seek(0)

    if output_type == "image":
        return StreamingResponse(response, media_type="image/png")

    else:
        warn(f"response is io but expected output type {output_type} which is not supported.")

    return response


def __convert_string_response(response: str):
    if not os.path.exists(response):
        return response

    try:
        if pathlib.Path(response).is_file():
            file_to_stream = open(response, "rb")

            out = StreamingResponse(file_to_stream, media_type=get_file_type(response))

            os.remove(response)

            return out

        else:
            return response

    except OSError as os_error:
        warn(f"Couldn't interpret stream: {os_error}")

        return response


def cast_response(response, expected_output: dict):
    """Cast model response to the expected output type

    Args:
        response (Any): response of the model
        expected_output (dict): dict describing the expected output

    Returns:
        Any: Casted response
    """

    if isinstance(response, PIL.Image.Image):
        return __convert_pillow_image_response(response)

    elif isinstance(response, np.ndarray):
        return __convert_ndarray_response(response, expected_output["type"])

    elif isinstance(response, bytes):
        return __convert_bytes_response(response, expected_output["type"])

    elif isinstance(response, io.IOBase):
        return __convert_io_response(response, expected_output["type"])

    elif isinstance(response, list):
        return json.dumps(response, cls=NpEncoder, ensure_ascii=False).encode('utf8')

    elif isinstance(response, str):
        return __convert_string_response(response)

    elif isinstance(response, bool) or isinstance(response, float):
        return response

    warn(f"Response type not supported ({type(response)}), returning a stream")

    ioresult = response
    ioresult.seek(0)

    return StreamingResponse(ioresult, media_type="image/png")
