import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

# 1. membuat objek dengan nama cap, untuk menampung video
cap = cv2.VideoCapture('test_video.webm')

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # result_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # result_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Displaythe resulting rame
    cv2.imshow('frame', result_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Ketika semuanya telah selesai, release the capture
cap.release()
cv2.destroyAllWindows()