import cv2
import numpy as np

# https://www.geeksforgeeks.org/background-subtraction-in-an-image-using-concept-of-running-average/

'''
Background subtraction is a technique for separating out foreground elements from the background and is done by generating a foreground mask.
This technique is used for detecting dynamically moving objects from static cameras.
Background subtraction technique is important for object tracking.
There are several techniques for background subtraction



The parameters passed in this function are :

cv2.accumulateWeighted(src, dst, alpha)

src: The source image. The image can be colored or grayscaled image and either 8-bit or 32-bit floating point.
dst: The accumulator or the destination image. It is either 32-bit or 64-bit floating point.
note: It should have the same channels as that of the source image. Also, the value of dst should be predeclared initially.
alpha: Weight of the input image. Alpha decides the speed of updating. If you set a lower value for this variable,
running average will be performed over a larger amount of previous frames and vice-versa.

hasilnya keren juga, kaya efek slow motion
'''

# capture frames from a camera
cap = cv2.VideoCapture(0)
  
# read the frames from the camera
_, img = cap.read()
  
# modify the data type
# setting to 32-bit floating point
averageValue1 = np.float32(img)
  
# loop runs if capturing has been initialized. 
while(1):
    # reads frames from a camera 
    _, img = cap.read()
      
    # using the cv2.accumulateWeighted() function
    # that updates the running average
    # cv2.accumulateWeighted(img, averageValue1, 0.02)
    cv2.accumulateWeighted(img, averageValue1, 0.1)
      
    # converting the matrix elements to absolute values 
    # and converting the result to 8-bit. 
    resultingFrames1 = cv2.convertScaleAbs(averageValue1)
  
    # Show two output windows
    # the input / original frames window
    cv2.imshow('InputWindow', img)
  
    # the window showing output of alpha value 0.02
    cv2.imshow('averageValue1', resultingFrames1)
      
    # Wait for Esc key to stop the program 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
cap.release() 
    
# De-allocate any associated memory usage 
cv2.destroyAllWindows()