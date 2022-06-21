from PIL import Image
from gladia_api_utils.io import _open


ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']


def resize_image(image: Image, new_width: int = 100) -> Image:
    """
    Resizes the image into the final width while maintaining aspect ratio

    :param image: image to resize
    :param new_width: target width
    :return: image resized with the new width
    """

    (width, height) = image.size

    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))

    return new_image


def convert_image_to_ascii(image: Image, buckets: int = 255 // (len(ASCII_CHARS) - 1)) -> str:
    """
    Replace every pixel with a character whose intensity is similar

    :param image: image to convert to ascii
    :param buckets: range of pixels associated to each ascii character
    :return: the ascii image converted to ascii characters
    """

    (width, _) = image.size

    initial_pixels = list(image.getdata())

    # convert pixels to ascii characters
    ascii_characters = ''.join([ASCII_CHARS[pixel_value // buckets] for pixel_value in initial_pixels])

    # Split the image in multiple list (one by row)
    ascii_image = [ascii_characters[index:index + width] for index in range(0, len(ascii_characters), width)]

    return '\n'.join(ascii_image)


def predict(image: bytes) -> str:
    """
    Transform an image to ascii characters

    :param image: image to transform
    :return: image in ascii characters
    """

    new_width = 100

    image = _open(image)

    image = resize_image(image, new_width=new_width)
    new_image = convert_image_to_ascii(image.convert('L'))

    return new_image
