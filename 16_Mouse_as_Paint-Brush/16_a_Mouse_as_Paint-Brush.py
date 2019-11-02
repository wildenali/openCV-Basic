import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html

"""
jadi cara kerjanya gini
klik kiri mouse dua kali pada window yang muncul
nanti akan ter create lingkarang warna biru.
"""

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:        # Left Button Double Click
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('gambar')
cv2.setMouseCallback('gambar', draw_circle)

while (1):
    cv2.imshow('gambar', img)
    if cv2.waitKey(20) & 0xFF == 27:    # ketika di pencet ESC maka dia keluar
        break

cv2.destroyAllWindows()