import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

# RESIZE
"""
Cara mengubah ukuran gambar
"""

img = cv2.imread('22_Messi.jpg')

res = cv2.resize(img,None,fx=5,fy=5,interpolation = cv2.INTER_CUBIC)
cv2.imshow('img dikali 5',res)

# OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('img dikali 2',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
