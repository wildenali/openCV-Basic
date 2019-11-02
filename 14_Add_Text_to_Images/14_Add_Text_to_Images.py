import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# Create a block image
img = np.zeros((512,512,3), np.uint8)

# Adding Text to Images:
"""
To put texts in images, you need specify following things
1. Text data that you want to write
2. Position coordinates of where you put it
3. Font type (Checkcv2.utText() docs for supported fonts)
4. Font Scale
5. Regular thins like color, thiockness, lineType etc. for better look lineType = cv2.LINE_AA is recommended
"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Coba Ini',(50,500), font, 3, (255,255,255),2,cv2.LINE_AA)

cv2.imshow('hasilnya', img)

cv2.waitKey(0)
cv2.destroyAllWindows()