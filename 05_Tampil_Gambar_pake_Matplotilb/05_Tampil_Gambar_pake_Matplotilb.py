import numpy as np
import cv2
from matplotlib import pyplot as plt    # tambahan untuk latihan no 05_Tampil_Gambar_pake_Matplotilb

# 1. membuat objek dengan nama img, untuk menampung gambarnya
img = cv2.imread('test_gambar.png', 1)      # kalau nilainya 1 -> berwarna, kalau 0 jadi hitam putih

# 5. cara menampilkan gambar dengan tambahan Matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])     # to hide tick values on X and Y axis
plt.show()