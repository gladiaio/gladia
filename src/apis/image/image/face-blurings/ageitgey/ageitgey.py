import cv2
from gladia_api_utils.file_management import input_to_files
from gladia_api_utils.image_management import blur_image
from numpy import ndarray


@input_to_files
def predict(image: bytes) -> ndarray:
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

    is_successful, im_png = cv2.imencode(".png", image)

    if is_successful:
        return im_png

    raise Exception("Error encoding image")
