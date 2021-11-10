import cv2
import numpy as np

image = cv2.imread('erode_1.png')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Using cv2.erode() method
imageResult = cv2.erode(image, kernel)
cv2.imshow('HASIL', imageResult)

cv2.waitKey(0)
cv2.destroyAllWindows()