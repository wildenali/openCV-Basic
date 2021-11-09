import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# 1. membuat objek dengan nama img, untuk menampung gambarnya
img = cv2.imread('test_gambar.png', 1)      # kalau nilainya 1 -> berwarna, kalau 0 jadi hitam putih

# 2. cara menampilkan gambar si objek img
cv2.imshow('gambarnya', img)

# 3. cara nge write gambar atau nge save/save as gambar
cv2.imwrite('gambar_baru.png', img)

for i in range(0,5):
    nama_gambar = 'gambar_baru' + '_' + str(i) + '.png'
    print(nama_gambar)
    cv2.imwrite(nama_gambar, img)    

# 3. test save gambar menjadi hitam putih
img_hitam_putih = cv2.imread('test_gambar.png', 0)
cv2.imwrite('gambar_hitam_putih.png', img_hitam_putih)

cv2.waitKey(0)
cv2.destroyAllWindows()