import io
import os
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
import requests
import tensorflow.compat.v1 as tf
from unifai_api_utils.image_management import draw_segment
from unifai_api_utils.model_management import download_models
from unifai_api_utils.io import _open
from PIL import Image
from skimage.filters import gaussian
from icecream import ic

sess = None

urls = {
    "xception": {
        "url": "https://huggingface.co/databuzzword/xception",
        "output_path": "models",
    }
}

models_path = download_models(urls)

ic(models_path)

# using xcetpion checkpoint 00000
current_model_path = os.path.join(models_path["xception"]["output_path"], "00000")
ic(current_model_path)


def run(image, fast=True):
    global sess
    sess = tf.Session()
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

    return resized_image, seg_map


def predict(image):
    image = _open(image)
    resized_im, seg_map = run(image, True)

    img = draw_segment(resized_im, seg_map)
    return img
