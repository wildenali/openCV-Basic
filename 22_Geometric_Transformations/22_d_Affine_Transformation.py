import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html

# Affine Transformation
"""
Transformation Affine adalah transformasi yang sering digunakan untuk  mentransformasikan nilai-nilai
kordinat dari suatu sistem kordinat dua dimensi ke sistem kordinat dua dimensi lainya.

Contohnnya gini deh
ada sebuah bangun segi empat dengan panjang 2 cm dan lebar 2 cm di koordinat x=0 dan y=0
kemudian di Affine Transformasikan sehingga hasilnya menjadi
panjang 3 cm dan lebar 8 cm dan di koordinat x=10, y=5

Nah itu ada perubahan kan dari segi empat menjadi persegi panjang, dan posisinya berubah juga
nah itu merukan contoh dari Affine Transformation
"""

img = cv2.imread('22_Messi.jpg',0)
rows, cols = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()