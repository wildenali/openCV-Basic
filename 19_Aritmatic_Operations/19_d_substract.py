import cv2
import numpy as np

# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-1-addition-and-subtraction/

# path to input images are specified and image are loaded with imread command
image1 = cv2.imread('cc.jpg')
image2 = cv2.imread('dd.jpg')

# cv2.addWeighted is applied over the image inputs with applied parameters
substractResult = cv2.subtract(image1, image2,)

cv2.imshow('result', substractResult)

cv2.waitKey(0)
cv2.destroyAllWindows()