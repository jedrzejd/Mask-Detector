from imutils.video import VideoStream

import imutils
import cv2

from config import resolution
from detection.mask_detection import mask_detection


vs = VideoStream().start()
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=resolution)

    frame = mask_detection(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
