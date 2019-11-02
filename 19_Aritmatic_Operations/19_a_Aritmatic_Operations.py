import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html

# Image Blending
img1 = cv2.imread('ml.jpg')
img2 = cv2.imread('opencv_logo.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()