
import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/python-visualizing-image-in-different-color-spaces/

'''
Cara mengubah-ubah warna gambar
'''

img = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/download5.png')
# img = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')


# # We can alternatively convert
# # image by using cv2color
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# # Shows the image
# cv2.imshow('image', img) 

# plt.imshow(img)
# plt.show()
  
# cv2.waitKey(0)         
# cv2.destroyAllWindows()


# Test 2 -----------------------------------------------------------
# Converts to HSV color space
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Converts to LAB color space
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
  
# Shows the image
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('EdgeMap', laplacian) 
  
cv2.waitKey(0)         
cv2.destroyAllWindows()