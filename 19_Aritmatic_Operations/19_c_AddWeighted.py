import cv2
import numpy as np

# https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-1-addition-and-subtraction/

# path to input images are specified and image are loaded with imread command
image1 = cv2.imread('aa.jpg')
image2 = cv2.imread('bb.jpg')

# cv2.addWeighted is applied over the image inputs with applied parameters
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
# 0.5 is weight og the image1
# 0.4 is weight og the image2
# 0 is gemmaValue which is measurement of light

cv2.imshow('result', weightedSum)

cv2.waitKey(0)
cv2.destroyAllWindows()