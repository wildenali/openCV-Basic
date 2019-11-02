import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('gambar')

# Create trackbar for color change
cv2.createTrackbar('R','gambar',0,255,nothing)
cv2.createTrackbar('G','gambar',0,255,nothing)
cv2.createTrackbar('B','gambar',0,255,nothing)

# Create switch for ON/OFF functionality
switch = '0 : OFF \n1: ON'
cv2.createTrackbar(switch,'gambar',0,1,nothing)

while(1):
    cv2.imshow('gambar', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','gambar')
    g = cv2.getTrackbarPos('G','gambar')
    b = cv2.getTrackbarPos('B','gambar')
    s = cv2.getTrackbarPos(switch,'gambar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()