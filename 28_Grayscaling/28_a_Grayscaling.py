import cv2
import numpy as np

# https://www.geeksforgeeks.org/python-grayscaling-of-images-using-opencv/

'''
Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray. It varies between complete black and complete white.

Importance of grayscaling 
Dimension reduction: For example, In RGB images there are three color channels and has three dimensions while grayscale images are single-dimensional.
Reduces model complexity: Consider training neural article on RGB images of 10x10x3 pixel. The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input nodes for grayscale images.
For other algorithms to work: Many algorithms are customized to work only on grayscale images e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscale images only.
'''

image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')

# Use the cvtColor() function to convert from the color to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('COLOR_BGR2GRAY', gray_image)

# Use the second argument or (flag value) zero, that specifies the image is to be read in grayscale mode
img = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg', 0)
cv2.imshow('Grayscale Image using 0', img)

# Using the pixel manipulation (Average method)
img = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')
# Obtain the dimensions of the image array
# using the shape method
(row, col) = img.shape[0:2]
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        img[i, j] = sum(img[i, j]) * 0.33
cv2.imshow('Pixel Manipulation', img)

cv2.waitKey(0)
cv2.destroyAllWindows()