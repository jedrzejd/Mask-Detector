from tensorflow.python.keras.models import load_model

import cv2

prototxtPath = "models/deploy.prototxt"
weightsPath = "models/face_model.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

maskNet = load_model("models/mask_detection.hdf5")

input_shape = (-1, 200, 200, 1)