import numpy as np
import cv2

# 1. membuat objek dengan nama img, untuk menampung gambarnya
img = cv2.imread('test_gambar.png', 1)      # kalau nilainya 1 -> berwarna, kalau 0 jadi hitam putih

# 2. cara menampilkan gambar si objek img
cv2.imshow('gambarnya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()