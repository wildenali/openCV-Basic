import cv2
import numpy as np

# https://www.geeksforgeeks.org/python-image-blurring-using-opencv/

image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')

# Gaussian Blurr
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)

# Median Blur
Median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', Median)

# Bilateral Blur
Bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', Bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()