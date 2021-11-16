
import cv2
import numpy as np

# https://www.geeksforgeeks.org/circle-detection-using-opencv-python/

'''
To detect circles, we may fix a point (x, y). Now, we are required to find 3 parameters: a, b and r.
Therefore, the problem is in a 3-dimensional search space. To find possible circles,
the algorithm uses a 3-D matrix called the “Accumulator Matrix” to store potential a, b and r values.
The value of a (x-coordinate of the center) may range from 1 to rows, b (y-coordinate of the center) may range from 1 to cols,
and r may range from 1 to maxRadius = \sqrt{rows^2 + cols^2}.
'''

# Reading image from folder where it is stored
img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/Detected-Circle.png')
# img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/image_2.jpg')
  
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))
  
# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
  
# Draw circles that are detected.
if detected_circles is not None:
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (255, 0, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()