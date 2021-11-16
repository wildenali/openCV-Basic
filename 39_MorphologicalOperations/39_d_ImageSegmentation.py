import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/image-segmentation-using-morphological-operation/

'''
If we want to extract or define something from the rest of the image, eg. detecting an object from a background,
we can break the image up into segments in which we can do more processing on. This is typically called Segmentation.

Morphological operations are some simple operations based on the image shape. It is normally performed on binary images.
Two basic morphological operators are Erosion and Dilation. For basic understanding about Dilation and Erosion


Approach :

Label the region which we are sure of being the foreground or object with one color (or intensity),
Label the region which we are sure of being background or non-object with another color.
Finally the region which we are not sure of anything, label it with 0. That is our marker. Then apply watershed algorithm.
Then our marker will be updated with the labels we gave, and the boundaries of objects will have a value of -1.
'''

# Reading image from folder where it is stored
img = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/coin-detection.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


# Noise removal using Morphological
# closing operation
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations = 2)

# Background area using Dialation
bg = cv2.dilate(closing, kernel, iterations = 1)
 
# Finding foreground area
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
ret, fg = cv2.threshold(dist_transform, 0.02 * dist_transform.max(), 255, 0)
  


cv2.imshow('Original', img)
cv2.imshow('thresh', thresh)
cv2.imshow('Morphological', fg)



cv2.waitKey(0)
cv2.destroyAllWindows()