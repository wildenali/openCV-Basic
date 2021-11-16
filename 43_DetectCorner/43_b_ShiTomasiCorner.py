
import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/circle-detection-using-opencv-python/

'''
Shi-Tomasi Corner Detection was published by J.Shi and C.Tomasi in their paper ‘Good Features to Track‘.
Here the basic intuition is that corners can be detected by looking for significant change in all direction.

Syntax : cv2.goodFeaturesToTrack(gray_img, maxc, Q, minD)

Parameters :
gray_img – Grayscale image with integral values
maxc – Maximum number of corners we want(give negative value to get all the corners)
Q – Quality level parameter(preferred value=0.01)
maxD – Maximum distance(preferred value=10)
'''

# Reading image from folder where it is stored
# img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/corner1.png')
img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/corner4.png')

# convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Shi-Tomasi corner detection function
# We are detecting only 100 best corners here
# You can change the number to get desired result.
corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10)
  
# convert corners values to integer
# So that we will be able to draw circles on them
corners = np.int0(corners)
  
# draw red color circles on all corners
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
  
# resulting image
plt.imshow(img)
plt.show()

# De-allocate any associated memory usage  
# if cv2.waitKey(0) & 0xff == 27: 
#     cv2.destroyAllWindows()
# cv2.waitKey(0)
# cv2.destroyAllWindows()