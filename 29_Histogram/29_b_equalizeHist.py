import cv2
import numpy as np

# https://www.geeksforgeeks.org/histograms-equalization-opencv/

'''
This method usually increases the global contrast of many images,
especially when the usable data of the image is represented by close contrast values.
Through this adjustment, the intensities can be better distributed on the histogram.
This allows for areas of lower local contrast to gain a higher contrast.
Histogram equalization accomplishes this by effectively spreading out the most frequent intensity values.
The method is useful in images with backgrounds and foregrounds that are both bright or both dark.
'''

image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/flower.png', 0)

#  creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(image)
  
# stacking images side-by-side
res = np.hstack((image, equ))
  
# show image input vs output
cv2.imshow('image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()