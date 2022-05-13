import os
from skimage.filters import gaussian
from PIL import Image
import numpy as np
import cv2


def compress_JPG_image(image, path_original, size=(1920, 1080)) -> str:
    """Convert a given file to JPG file"""
    width, height = size

    name = os.path.basename(path_original).split(".")
    first_name = os.path.join(os.path.dirname(path_original), name[0] + ".jpg")

    if image.size[0] > width and image.size[1] > height:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(first_name, quality=85)
    elif image.size[0] > width:
        wpercent = width / float(image.size[0])
        height = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(first_name, quality=85)
    elif image.size[1] > height:
        wpercent = height / float(image.size[1])
        width = int((float(image.size[0]) * float(wpercent)))
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(first_name, quality=85)
    else:
        image.save(first_name, quality=85)

    return first_name


def convert_to_JPG(path_original) -> str:
    """Convert a given file to JPG file"""
    img = Image.open(path_original)
    name = os.path.basename(path_original).split(".")
    first_name = os.path.join(os.path.dirname(path_original), name[0] + ".jpg")

    if img.format == "JPEG":
        image = img.convert("RGB")
        compress_JPG_image(image, path_original)
        img.close()

    elif img.format == "GIF":
        i = img.convert("RGBA")
        bg = Image.new("RGBA", i.size)
        image = Image.composite(i, bg, i)
        compress_JPG_image(image, path_original)
        img.close()

    elif img.format == "PNG":
        try:
            image = Image.new("RGB", img.size, (255, 255, 255))
            image.paste(img, img)
            compress_JPG_image(image, path_original)
        except ValueError:
            image = img.convert("RGB")
            compress_JPG_image(image, path_original)

        img.close()

    elif img.format == "BMP":
        image = img.convert("RGB")
        compress_JPG_image(image, path_original)
        img.close()

    return path_original


def blur_image(image, x0, x1, y0, y1, sigma=1, multichannel=True):
    """Square blur in image"""
    y0, y1 = min(y0, y1), max(y0, y1)
    x0, x1 = min(x0, x1), max(x0, x1)
    im = image.copy()
    sub_im = im[y0:y1, x0:x1].copy()
    blur_sub_im = gaussian(sub_im, sigma=sigma, multichannel=multichannel)
    blur_sub_im = np.round(255 * blur_sub_im)
    im[y0:y1, x0:x1] = blur_sub_im
    return im


def draw_segment(baseImg, matImg):
    width, height = baseImg.size
    dummyImg = np.zeros([height, width, 4], dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            color = matImg[y, x]
            (r, g, b) = baseImg.getpixel((x, y))
            if color == 0:
                dummyImg[y, x, 3] = 0
            else:
                dummyImg[y, x] = [r, g, b, 255]
    img = Image.fromarray(dummyImg)
    return img
