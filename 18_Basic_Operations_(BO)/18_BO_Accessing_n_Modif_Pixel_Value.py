import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html


img = cv2.imread('roi.jpg')

# you can access a pixel value by its row and columnd coorinates
# for BGR image, it returns an array of Blue, Gree, Red values
# for Grayscale image, just coresponding intensity is returned

px = img[100,100]
print px

# accessing only blue pixel
blue = img[100,100,0]
print blue

# Modif the pixel value
img[100,100] = [255,255,255]
print img[100,100]

# Accessing RED value
img.item(10,10,2)
print img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)
print img.item(10,10,2)

# Accessing Image Properties
print img.shape
print img.size
print img.dtype     # ini sangat penting, karena kebanyakan kasus error di OpenCV karena salah tipe data

# Image ROI (Region of Images)
# beluuum, tutorial di link nya error hasilnya