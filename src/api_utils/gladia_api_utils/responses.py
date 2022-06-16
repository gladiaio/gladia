from fastapi.responses import Response

class ImageResponse(Response):
    media_type = "image/*"

    schema = {
        "type":"string",
        "format": "binary"
    }


class AudioResponse(Response):
    media_type = "audio/*"

    schema = {
        "type":"string",
        "format": "binary"
    }


class VideoResponse(Response):
    media_type = "video"

    schema = {
        "type":"string",
        "format": "binary"
    }

