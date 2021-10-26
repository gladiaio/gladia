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
from icecream import ic
from PIL import Image
from skimage.filters import gaussian

tf.disable_v2_behavior()


urls = {
    "mobile-net": {
        "url": "https://huggingface.co/databuzzword/mobile-net",
        "output_path": "models",
    }
}

models_path = download_models(urls)

# using mobile-net 30K checkpoint
current_model_path = os.path.join(models_path["mobile-net"]["output_path"], "30000")


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
    ic(graph_path)
    slow_graph_def = tf.GraphDef.FromString(open(graph_path, "rb").read())

    tf.import_graph_def(slow_graph_def, name="")

    batch_seg_map = sess.run(
        sess.graph.get_tensor_by_name(OUTPUT_TENSOR_NAME),
        feed_dict={INPUT_TENSOR_NAME: [np.asarray(resized_image)]},
    )

    seg_map = batch_seg_map[0]

    return resized_image, seg_map


def predict(image):
    
    image = Image.open(BytesIO(image))
    resized_im, seg_map = run(image, True)

    img = draw_segment(resized_im, seg_map)

    return img
