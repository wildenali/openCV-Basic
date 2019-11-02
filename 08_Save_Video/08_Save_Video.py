import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

# membuat objek dengan nama cap, untuk menampung gambar dari kamera webcam
cap = cv2.VideoCapture(0)

# Mendefinisikan codec dan membuat VideoWriter objek
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))


while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        frame = cv2.flip(frame,0)   # gambarnya di flip, untuk tidak di flip, pake fungsi 

        #write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Ketika semuanya telah selesai, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()