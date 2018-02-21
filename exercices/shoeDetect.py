import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = cv2.VideoCapture("../dataset/examples-video/test.mp4")
template = cv2.imread('../dataset/examples/shoeTemplate.png',0)
w, h = template.shape[::-1]
methods = 'cv2.TM_CCOEFF_NORMED'
kernel = np.ones((3, 3), np.uint8)


while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame1 = cv2.morphologyEx(frame1, cv2.MORPH_OPEN, kernel)
    frame1  = cv2.morphologyEx(frame1, cv2.MORPH_CLOSE,kernel)
    #frame1 = cv2.adaptiveThreshold(frame1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    frame1 = cv2.Canny(frame1, 30, 70)
    # Apply template Matching
#     method = eval(methods)
#     res = cv2.matchTemplate(frame1,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     bottom_right = (max_loc[0] + w, max_loc[1] + h)
#     cv2.rectangle(frame1,max_loc, bottom_right, 255, 2)
    
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()