import cv2
import numpy as np

# https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/

'''
Intensity transformations are applied on images for contrast manipulation or image thresholding.
These are in the spatial domain, i.e. they are performed directly on the pixels of the image at hand,
as opposed to being performed on the Fourier transform of the image.

1. Image Negatives (Linear)
2. Log Transformations
3. Power-Law (Gamma) Transformations
4. Piecewise-Linear Transformation Functions
'''

# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

# Reading image from folder where it is stored
img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/sample.jpg')

# Define parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)
  
# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

cv2.imshow('Real Image _3', img)
cv2.imshow('contrast_stretched', contrast_stretched)

cv2.waitKey(0)
cv2.destroyAllWindows()