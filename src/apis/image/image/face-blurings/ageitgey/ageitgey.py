from io import BytesIO

from gladia_api_utils.file_management import input_to_files
from gladia_api_utils.image_management import blur_image
from gladia_api_utils.io import np_to_img_buffer


@input_to_files
def predict(image: bytes) -> BytesIO:
    """
    Call the model returning the image with the faces blured

    :param image: the image to blur the faces from
    :return: the image with the faces blured
    """

    import face_recognition

    sigma = 50

    image = face_recognition.load_image_file(image)

    locations = face_recognition.face_locations(image)

    for location in locations:
        (startY, endY) = location[0:2]
        (startX, endX) = location[2:4]

        image = blur_image(image, startX, endX, startY, endY, sigma=sigma)

    return np_to_img_buffer(image)
