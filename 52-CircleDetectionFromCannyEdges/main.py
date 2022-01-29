import cv2
import cvzone
import numpy as np
import imutils

# cap             = cv2.VideoCapture(1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap.set(cv2.CAP_PROP_AUTOFOCUS, 1) # turn the autofocus off
# cap.set(28, 172)    # 177 is focus value of razer camera

cap             = cv2.VideoCapture('cek_video3.mp4')

frameCounter    = 0
cornerPoints    = [[10, 200], [650, 200], [10, 550], [650, 550]]     # ini kordinat soalnya gambarnya mau di pas in disini
# [39, 263], [721, 263], [39, 649], [717, 649]



def getBoard(img):
    # width, height = int(400*1.5), int(380*1.5)  # unit milimeter
    # width, height = int(400), int(380)  # unit milimeter
    width, height = int(845), int(480)  # unit milimeter
    pts1 = np.float32(cornerPoints)
    pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)    # creating matrix
    imgOutput = cv2.warpPerspective(img, matrix, (width,height))    # transform the img

    return imgOutput

def detectCircle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 10, 70)
    ret, mask = cv2.threshold(canny, 200, 255, cv2.THRESH_BINARY)
    cv2.imshow('canny', canny)
    cv2.imshow('mask', mask)

    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 2, 20, param1=50, param2=30, minRadius=0, maxRadius=10)
    
    # ensure at least some circles were found
    if circles is not None:
        # print("Lingkaran Ada")
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        
        # print(circles[0])
        # print(circles[1])
        # print(len(circles))

        # loop over the (x, y) coordinates and radius of the circles
        i = 0
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            # cv2.circle(mask, (x, y), r, (0, 255, 0), 4)
            # cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            print("Lingkaran Ada ", "Circle:", i, "x:", x, "y:", y, "Radius:", r)
            i+=1
            # print(x)
            # print("Row Number: ")
            # print(y)
            # print("Radius is: ")
            # print(r)
    else:
        print("Lingkaran Tidak Ada")
    
    return img


while True:
   
    success, img = cap.read()
    
    imgBoard = getBoard(img)
    mask = detectCircle(imgBoard)
    
    # cv2.imshow('Image', img)
    cv2.imshow('imgBoard',  imgBoard)
    # cv2.imshow('mask',  mask)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()