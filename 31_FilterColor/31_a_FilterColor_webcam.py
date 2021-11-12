import cv2
import numpy as np

# https://www.geeksforgeeks.org/filter-color-with-opencv/

'''
For color segmentation, all we need is the threshold values or the knowledge of the lower bound and
upper bound range of colors in one of the color spaces. It works best in the Hue-Saturation-Value color space. 
After specifying the range of color to be segmented, it is needed to create a mask accordingly and by using it,
a particular region of interest can be separated out.
'''

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    # It converts the RGB color space of image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold of blue in HSV space
    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])

    # Preparing the mask to overlay
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # The black region in the mask has the value of 0
    # so when multiplied with original image removes all non-blue regions
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
     
    cv2.waitKey(0)


cv2.destroyAllWindows()
cap.release()