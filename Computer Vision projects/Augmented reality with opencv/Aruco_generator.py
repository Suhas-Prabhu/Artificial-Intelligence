import numpy as np
import cv2

# load the predefined model
ar_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# generate the markers
marker_image = np.zeros((200,200),dtype=np.uint8)
marker_image = cv2.aruco.drawMarker(ar_dict, 36, 200, marker_image, 1)

cv2.imwrite('Artificial-Intelligence/Computer Vision projects/Augmented reality with opencv/marker36.png',marker_image)