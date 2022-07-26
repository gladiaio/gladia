import numpy as np


def text_to_numpy(text: str) -> np.array:
    """Cast test into np byte array

    Args:
        text (str): text to cast

    Returns:
        np.array: casted text
    """

    np_array = np.array([text.encode("utf-8")])

    np_array = np.expand_dims(np_array, axis=0)

    return np.array(
        [str(x).encode("utf-8") for x in np_array.reshape(np_array.size)],
        dtype=np.object_,
    )
