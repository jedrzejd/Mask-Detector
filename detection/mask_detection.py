from detection.face_detection import face_detector
from detection.mask_prediction import mask_prediction
from model import faceNet

import cv2

import numpy as np


def mask_detection(frame):
    (locs, faces) = face_detector(frame, faceNet)
    preds = mask_prediction(faces)
    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        if np.argmax(pred) == 0:
            label = 'Mask'
        else:
            label = 'No Mask'
        print(label)
        if label == "Mask":
            cl = (0, 255, 0)
        else:
            cl = (0, 0, 255)

        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv2.putText(frame, label, (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, cl, 2)
        cv2.rectangle(frame, (startX, startY), (endX, endY), cl, 2)

    return frame
