
import cv2
import numpy as np
import imutils

# https://www.geeksforgeeks.org/python-document-field-detection-using-template-matching/

'''
Approach:

Clip/Crop field images from the main document and use them as separate templates.
Define/tune thresholds for different fields.
Apply template matching for each cropped field template using OpenCV function cv2.matchTemplate()
Draw bounding boxes using the coordinates of rectangles fetched from template matching.
Optional: Augment field templates and fine tune threshold to improve result for different document images.
'''

field_threshold = { "prev_policy_no" : 0.7,
                    "address"        : 0.7,
                  }

# Function to Generate bounding
# boxes around detected fields
def getBoxed(img, img_gray, template, field_name = "policy_no"):
  
    w, h = template.shape[::-1] 
  
    # Apply template matching
    res = cv2.matchTemplate(img_gray, template,
                           cv2.TM_CCOEFF_NORMED)
  
    hits = np.where(res >= field_threshold[field_name])
  
    # Draw a rectangle around the matched region. 
    for pt in zip(*hits[::-1]): 
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),
                                    (0, 255, 255), 2)
  
        y = pt[1] - 10 if pt[1] - 10 > 10 else pt[1] + h + 20
  
        cv2.putText(img, field_name, (pt[0], y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)
  
    return img
  
  
# Driver Function
if __name__ == '__main__':
  
    # Read the original document image
    img    = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/document_field.png')
    # img = cv2.imread('doc.png')
        
    # 3-d to 2-d conversion
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
    # Field templates
    template_add = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/doc_address.png', 0)
    template_prev = cv2.imread('/home/dewatic/Documents/openCV-Basic-with-Python/image_resources/doc_prev_policy.png', 0)
  
    img = getBoxed(img.copy(), img_gray.copy(), template_add, 'address')
  
    img = getBoxed(img.copy(), img_gray.copy(), template_prev, 'prev_policy_no')
  
    cv2.imshow('Detected', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()