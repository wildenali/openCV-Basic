import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html

# Measuring Performance with OpenCV
img1 = cv2.imread('messi.jpg')

e1 = cv2.getTickCount()
for i in xrange(5,39,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t