
import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/python-bilateral-filtering/

'''
A bilateral filter is used for smoothening images and reducing noise, while preserving edges.
This article explains an approach using the averaging filter, while this article provides one using a median filter.
However, these convolutions often result in a loss of important edge information, since they blur out everything,
irrespective of it being noise or an edge. To counter this problem, the non-linear bilateral filter was introduced.


OpenCV has a function called bilateralFilter() with the following arguments: 
d: Diameter of each pixel neighborhood.
sigmaColor: Value of \sigma  in the color space. The greater the value, the colors farther to each other will start to get mixed.
sigmaSpace: Value of \sigma  in the coordinate space. The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
'''

# Reading image from folder where it is stored
img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/contour_test.jpg')
# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
bilateral = cv2.bilateralFilter(img, 15, 75, 75)
 
# Save the output.
cv2.imwrite('taj_bilateral.jpg', bilateral)

cv2.imshow('Real Image _3', img)   
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()