
import cv2
import numpy as np

# https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/

'''
OpenCV helps us to control and manage different types of mouse events and gives us the flexibility to operate them.
There are many types of mouse events. These events can be displayed by running the following code segment :

import cv2
[print(i) for i in dir(cv2) if 'EVENT' in i]

EVENT_FLAG_ALTKEY
EVENT_FLAG_CTRLKEY
EVENT_FLAG_LBUTTON
EVENT_FLAG_MBUTTON
EVENT_FLAG_RBUTTON
EVENT_FLAG_SHIFTKEY
EVENT_LBUTTONDBLCLK
EVENT_LBUTTONDOWN
EVENT_LBUTTONUP
EVENT_MBUTTONDBLCLK
EVENT_MBUTTONDOWN
EVENT_MBUTTONUP
EVENT_MOUSEHWHEEL
EVENT_MOUSEMOVE
EVENT_MOUSEWHEEL
EVENT_RBUTTONDBLCLK
EVENT_RBUTTONDOWN
EVENT_RBUTTONUP



Algorithm :

Import the cv2 module.
Import the image using the cv2.imread() function.
Display the image the image using the cv2.imshow() function.
Call the cv2.setMouseCallback() function and pass the image window and the user-defined function as parameters.
In the user-defined function, check for left mouse clicks using the cv2.EVENT_LBUTTONDOWN attribute.
Display the coordinates on the Shell.
Display the coordinates on the created window.
Do the same for right mouse clicks using the cv2.EVENT_RBUTTONDOWN attribute. Change the color while displaying the coordinates on the image to distinguish from left clicks.
Outside the user-defined function, use the cv2.waitKey(0) and the cv2.destroyAllWindows() functions to close the window and terminate the program.
'''


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
 
# driver function
if __name__=="__main__":
 
    # reading the image
    # img = cv2.imread('lena.jpg', 1)
    img = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_1_600x400.jpg')
    
 
    # displaying the image
    cv2.imshow('image', img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()