import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

"""
jadi misal nih di tutorial 21_b_*** kan dia ngebahas threshold dengan menggunakan global value
nah itu tidak efektif kalau misalnya kondisi gambar nya misalnya di ambil dari kamera, dan\
ternyata cahaya lingkungan nya berubah-ubah, misal dari indoor ke outdoor
untuk itu ada cara lain yaitu dengan menggunakan Adaptive Thresholding
"""

"""
Adaptive Method - It decides how thresholding value is calculated.
- cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
- cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
"""

img = cv2.imread('21_c_Adaptive_Thresholding.jpg',0)
img = cv2.medianBlur(img,5)     # coba ubah angkanya dari 1-5


ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v=127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()