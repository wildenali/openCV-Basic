import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# Create a block image
img = np.zeros((512,512,3), np.uint8)

# Draw a Polygon
"""
to draw a polygon first you need coordinates of vertices.
Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32.
Here we draw a small polygon of with four vertices in yellow color
"""
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('hasilnya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()