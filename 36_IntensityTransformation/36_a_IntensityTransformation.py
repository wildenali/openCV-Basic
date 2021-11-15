
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

# Reading image from folder where it is stored
img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/sample.jpg')

# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
  
# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)

cv2.imshow('Real Image _3', img)
cv2.imshow('log_transformed', log_transformed)

# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
    cv2.imshow('gamma_transformed '+str(gamma)+'.jpg', gamma_corrected)


cv2.waitKey(0)
cv2.destroyAllWindows()