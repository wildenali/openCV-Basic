import cv2
import numpy as np

# https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-2-adaptive-thresholding

'''
In Simple Thresholding, a global value of threshold was used which remained constant throughout.
So, a constant threshold value won’t help in the case of variable lighting conditions in different areas.
Adaptive thresholding is the method where the threshold value is calculated for smaller regions.
This leads to different threshold values for different regions with respect to the change in lighting.
We use cv2.adaptiveThreshold for this.

Syntax: cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)

Parameters:
-> source: Input Image array(Single-channel, 8-bit or floating-point)
-> maxVal: Maximum value that can be assigned to a pixel.
-> adaptiveMethod: Adaptive method decides how threshold value is calculated.

 cv2.ADAPTIVE_THRESH_MEAN_C: Threshold Value = (Mean of the neighbourhood area values – constant value). In other words, it is the mean of the blockSize×blockSize neighborhood of a point minus constant.

cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Threshold Value = (Gaussian-weighted sum of the neighbourhood values – constant value). In other words, it is a weighted sum of the blockSize×blockSize neighborhood of a point minus constant.

-> thresholdType: The type of thresholding to be applied.
-> blockSize: Size of a pixel neighborhood that is used to calculate a threshold value.
-> constant: A constant value that is subtracted from the mean or weighted sum of the neighbourhood pixels.
'''

# image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/download5.png')
image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale 
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
# applying different thresholding 
# techniques on the input image
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 199, 5)
  
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 199, 5)
  
# the window showing output images
# with the corresponding thresholding 
# techniques applied to the input image
cv2.imshow('Real Image', image)
cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()