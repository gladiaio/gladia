import os

import numpy as np
import tensorflow.compat.v1 as tf
from gladia_api_utils.image_management import draw_segment
from gladia_api_utils.io import _open
from gladia_api_utils.model_management import download_models
from PIL import Image

sess = None

urls = {
    "xception": {
        "url": "https://huggingface.co/databuzzword/xception",
        "output_path": "models",
    }
}

models_path = download_models(urls)

# using xcetpion checkpoint 00000
current_model_path = os.path.join(models_path["xception"]["output_path"], "00000")


def run(image: Image, fast: bool = True) -> (Image, np.ndarray):
    """
    Call the model to return the image without its background

    :param image: Image to remove the background from
    :param fast: unused
    :return: image without its background
    """

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True

    sess = tf.Session(config=config)

    INPUT_TENSOR_NAME = "ImageTensor:0"
    INPUT_SIZE = 513
    FROZEN_GRAPH_NAME = "frozen_inference_graph"
    OUTPUT_TENSOR_NAME = "SemanticPredictions:0"

    width, height = image.size
    resize_ratio = 1.0 * INPUT_SIZE / max(width, height)
    target_size = (int(resize_ratio * width), int(resize_ratio * height))
    resized_image = image.convert("RGB").resize(target_size, Image.ANTIALIAS)

    graph_path = os.path.join(current_model_path, "frozen_inference_graph.pb")

    slow_graph_def = tf.GraphDef.FromString(open(graph_path, "rb").read())
    tf.import_graph_def(slow_graph_def, name="")

    batch_seg_map = sess.run(
        sess.graph.get_tensor_by_name(OUTPUT_TENSOR_NAME),
        feed_dict={INPUT_TENSOR_NAME: [np.asarray(resized_image)]},
    )

    seg_map = batch_seg_map[0]

    tf.reset_default_graph()
    sess.close()

    return resized_image, seg_map


def predict(image) -> Image:
    """
    Call the model to return the image without its background

    :param image: Image to remove the background from
    :return: image without its background
    """

    image = _open(image)

    resized_im, seg_map = run(image, True)

    img = draw_segment(resized_im, seg_map)

    return img
