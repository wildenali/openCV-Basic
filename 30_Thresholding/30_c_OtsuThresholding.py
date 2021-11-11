import cv2
import numpy as np

# https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-3-otsu-thresholding

'''
In Adaptive thresholding, the threshold value is calculated for smaller regions with different threshold values 
for different regions with respect to the change in lighting.

In Otsu Thresholding, a value of the threshold isn’t chosen but is determined automatically.
A bimodal image (two distinct image values) is considered. The histogram generated contains two peaks.
So, a generic condition would be to choose a threshold value that lies in the middle of both the histogram peak values.

Syntax: cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)

Parameters:
-> source: Input Image array (must be in Grayscale).
-> thresholdValue: Value of Threshold below and above which pixel values will change accordingly.
-> maxVal: Maximum value that can be assigned to a pixel.
-> thresholdingTechnique: The type of thresholding to be applied.
'''

image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/download5.png')
# image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# applying Otsu thresholding
# as an extra flag in binary 
# thresholding     
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + 
                                            cv2.THRESH_OTSU)     
  
# the window showing output image         
# with the corresponding thresholding         
# techniques applied to the input image    
cv2.imshow('Real Image', image)
cv2.imshow('Otsu Threshold', thresh1)   

cv2.waitKey(0)
cv2.destroyAllWindows()