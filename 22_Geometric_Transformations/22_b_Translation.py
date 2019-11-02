import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

# Translation
"""
Cara memindahkan gambar
"""

img = cv2.imread('22_Messi.jpg',0)
rows, cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()