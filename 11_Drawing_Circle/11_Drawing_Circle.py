import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# Create a block image
img = np.zeros((512,512,3), np.uint8)

# Draw a circle, you need its center coordinates and radius
img = cv2.circle(img,(447,63),63,(0,0,255),-1)

cv2.imshow('hasilnya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()