import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

# Create a block image
img = np.zeros((512,512,3), np.uint8)

# 09. Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# 10. Draw a rectangle blue, you need top-left corner and bottom-right corner of rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# 11. Draw a circle, you need its center coordinates and radius
img = cv2.circle(img,(447,63),63,(0,0,255),-1)

# 12. Ellipse
"""
to draw the ellipse, we need several arguments
1. center location (x,y)
2. axes length (major axis length, minor axis length)
3. angle is the angle of rotation of ellipse in ati-clockwise direction
4. startAngle and engAngle donates the starting and ending of ellipse arc measured in clockwise direction from major axis (0-360)
"""
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# 13. Draw a Polygon
"""
to draw a polygon first you need coordinates of vertices.
Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32.
Here we draw a small polygon of with four vertices in yellow color
"""
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# 14. Adding Text to Images:
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