import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# Create a block image
img = np.zeros((512,512,3), np.uint8)

"""
to draw the ellipse, we need several arguments
1. center location (x,y)
2. axes length (major axis length, minor axis length)
3. angle is the angle of rotation of ellipse in ati-clockwise direction
4. startAngle and engAngle donates the starting and ending of ellipse arc measured in clockwise direction from major axis (0-360)
"""
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

cv2.imshow('hasilnya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()