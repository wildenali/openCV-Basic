import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/opencv-python-program-analyze-image-using-histogram/

'''
The image should be used in a PNG file as matplotlib supports only PNG images. 
Here, It’s a 24-bit RGB PNG image (8 bits for each of R, G, B) used in this example. Each inner list represents a pixel.
Here, with an RGB image, there are 3 values. For RGB images, matplotlib supports float32 and uint8 data types.

Histogram is considered as a graph or plot which is related to frequency of pixels in an Gray Scale Image
with pixel values (ranging from 0 to 255).
Grayscale image is an image in which the value of each pixel is a single sample, that is,
it carries only intensity information where pixel value varies from 0 to 255. Images of this sort,
also known as black-and-white, are composed exclusively of shades of gray,
varying from black at the weakest intensity to white at the strongest where Pixel can be considered as a every point in an image.

Here, we get intuition about contrast, brightness, intensity distribution etc of that image.
As we can see the image and its histogram which is drawn for grayscale image, not color image.
Left region of histogram shows the amount of darker pixels in image and right region shows the amount of brighter pixels.

images : it is the source image of type uint8 or float32 represented as “[img]”.
channels : it is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and
color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
mask : mask image. To find histogram of full image, it is given as “None”.
histSize : this represents our BIN count. For full scale, we pass [256].
ranges : this is our RANGE. Normally, it is [0,256].
'''

image = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/flower.png')

# calculate frequency of pixels in range 0-255
histg = cv2.calcHist([image],[0],None,[256],[0,256]) 

plt.plot(histg)
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()