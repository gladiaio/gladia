import io
import json
import os
import pathlib
import re
from warnings import warn

import numpy as np
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from PIL import ExifTags, Image
from PIL.PngImagePlugin import PngInfo
from starlette.responses import StreamingResponse

from .file_management import get_file_type


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return obj.decode("utf-8")
        else:
            return super(NpEncoder, self).default(obj)


def __convert_pillow_image_response(
    image_response: Image.Image, additional_metadata: dict = dict()
):
    ioresult = io.BytesIO()

    image_response.save(ioresult, format="png")

    ioresult.seek(0)

    returned_response = StreamingResponse(ioresult, media_type="image/png")

    if len(additional_metadata) > 0:
        returned_response.headers["gladia_metadata"] = json.dumps(additional_metadata)

    return returned_response


def __convert_ndarray_response(response: np.ndarray, output_type: str):
    if output_type == "image":
        ioresult = io.BytesIO(response.tobytes())
        ioresult.seek(0)

        return StreamingResponse(ioresult, media_type="image/png")

    elif output_type == "text":
        return JSONResponse(content=jsonable_encoder(response.tolist()))

    else:
        warn(
            f"response is numpy array but expected output type {output_type} which is not supported."
        )

        return response


def __convert_bytes_response(response: bytes, output_type: str):
    ioresult = io.BytesIO(response)
    ioresult.seek(0)

    if output_type == "image":
        return StreamingResponse(ioresult, media_type="image/png")

    else:
        warn(
            f"response is bytes but expected output type {output_type} which is not supported."
        )

    return response


def __convert_io_response(response: io.IOBase, output_type: str):
    response.seek(0)

    if output_type == "image":
        return StreamingResponse(response, media_type="image/png")

    else:
        warn(
            f"response is io but expected output type {output_type} which is not supported."
        )

    return response


def __convert_string_response(response: str):
    # if response is a string but not a file path
    # try to load it as a json representation
    # else return it as is
    if not os.path.exists(response):
        try:
            # I decided to use regex instead of ast.literal_eval
            # for security reason.
            # having regex doesn't interpret while
            # ast.literal_eval will
            # see this proposition:
            # https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
            # which I found very risky
            # J.L
            p = re.compile("(?<!\\\\)'")
            this_response = p.sub('"', response)
            return json.loads(this_response)
        except:
            try:
                return {"prediction": str(response)}
            except Exception as e:
                warn(f"Couldn't interpret response returning plain response: {e}")
                return response

    # if the string looks like a filepath
    # try to load it as a json
    # else try to stream it
    else:
        try:
            if pathlib.Path(response).is_file():
                try:
                    return json.load(response)
                except Exception as e:
                    file_to_stream = open(response, "rb")
                    return StreamingResponse(
                        file_to_stream, media_type=get_file_type(response)
                    )
                finally:
                    os.remove(response)
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
    if isinstance(response, tuple):
        if list(map(type, response)) == [Image.Image, dict]:
            image, addition_exif = response
            return __convert_pillow_image_response(image, addition_exif)
        else:
            return json.loads(json.dumps(response, cls=NpEncoder, ensure_ascii=False))

    elif isinstance(response, Image.Image):
        return __convert_pillow_image_response(response)

    elif isinstance(response, np.ndarray):
        return __convert_ndarray_response(response, expected_output["type"])

    elif isinstance(response, (bytes, bytearray)):
        return __convert_bytes_response(response, expected_output["type"])

    elif isinstance(response, io.IOBase):
        return __convert_io_response(response, expected_output["type"])

    elif isinstance(response, (list, dict)):
        return json.loads(
            json.dumps(response, cls=NpEncoder, ensure_ascii=False).encode("utf8")
        )

    elif isinstance(response, str):
        return __convert_string_response(response)

    elif isinstance(response, bool) or isinstance(response, float):
        return {"prediction": str(response)}

    elif isinstance(response, int):
        return {"prediction": str(response)}

    warn(f"Response type not supported ({type(response)}), returning a stream")

    ioresult = response
    ioresult.seek(0)

    return StreamingResponse(ioresult, media_type="image/png")
