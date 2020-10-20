import numpy as np

from model import maskNet, input_shape


def mask_prediction(faces):
    preds = []

    if len(faces) > 0:
        faces = np.array(faces)
        faces = faces.reshape(input_shape)
        preds = maskNet.predict(faces)

    return preds