import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

# Perspective Transformation
"""
for perspective transformation, you need a 3x3 transformation matrix.
Straight lines will remain straight even after the transformation.
To find this transformation matrix, you need 4 points on the input image and corresponding points on the output image.
Among these 4 points, 3 of them should not e collinear.
Then transformation matrix can be found by the function cv2.getPerspectiveTransform.
Then apply cv2.warpPerspective with 3x3 transformation matrix
"""

img = cv2.imread('22_sudokusmall.png')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()