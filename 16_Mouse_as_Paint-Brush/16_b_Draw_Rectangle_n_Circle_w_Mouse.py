import cv2
import numpy as np

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html

"""
jadi cara kerjanya gini
ketika muncul window background hitam
coba klik kiri mouse nah itu akan keluar kotak warna hijau
kalau mau bentuk lingkarang, klik 'm' dulu di keyboard kemudian klik pada layar tersebut
nanti akan keluar lingkaran setiap setelah di klik
"""

drawing = False         # true is mouse pressed
mode = True             # if True, draw Rectangle. Press 'm' to toggle to curve
ix,iy = 1, -1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDBLCLK:
        drawing = True
        ix,iy = x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

        
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('gambar')
cv2.setMouseCallback('gambar', draw_circle)

while (1):
    cv2.imshow('gambar', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()