import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

# Rotation

img = cv2.imread('22_Messi.jpg',0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()