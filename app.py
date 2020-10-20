from imutils.video import VideoStream

import imutils
import cv2

from mask_detection import mask_detection


vs = VideoStream().start()
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=720)

    frame = mask_detection(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
