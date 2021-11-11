import cv2
import numpy as np

# https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/

'''
Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image. 
The most basic morphological operations are two: Erosion and Dilation

'''

# Reading the input image
img = cv2.imread('erode_1.png', 0)
 
# Taking a matrix of size 5 as the kernel
kernel = np.ones((5,5), np.uint8)
 
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
 
cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()