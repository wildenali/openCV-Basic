
import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/

'''
'''

# Reading image from folder where it is stored
img2    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/contour_test.jpg')
font    = cv2.FONT_HERSHEY_COMPLEX

# Reading same image in another, variable and converting to gray scale.
img     = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/contour_test.jpg', cv2.IMREAD_GRAYSCALE)

# Converting image to a binary image, ( black and white only image).
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

# Detecting contours in image.
contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('Real Image', img2)   
cv2.imshow('IMREAD_GRAYSCALE', img)
cv2.imshow('threshold', threshold)
# print(contours)

# Going through every contours found in the image.
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel()
    print(n)
    i = 0

    for j in n:
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
  
            # String containing the co-ordinates.
            string = str(x) + " " + str(y)
            print(string)

            cv2.imshow('Real Image _2', img2)   
            cv2.imshow('IMREAD_GRAYSCALE _2', img)
            cv2.imshow('threshold _2', threshold)

            if(i == 0):
                # text on topmost co-ordinate.
                cv2.putText(img2, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))
            else:
                # text on remaining co-ordinates.
                cv2.putText(img2, string, (x, y), font, 0.5, (0, 255, 0))
        i = i + 1
    

cv2.imshow('Real Image _3', img2)   
cv2.imshow('IMREAD_GRAYSCALE _3', img)
cv2.imshow('threshold _3', threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()