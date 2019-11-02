import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html

# Bitwise Operations
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv_logo.jpg')

# i want to put logo on top-lef corner, so i create ROI
rows,cols,channels = img2.shape
roi  = img1[0:rows, 0:cols]

# now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2,img1,mask = mask)

#put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()