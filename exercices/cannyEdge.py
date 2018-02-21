import cv2
import numpy as np


cap = cv2.VideoCapture("../dataset/examples-video/test.mp4")
#ret, frame = cap.read()


while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #ret, frame1 = cv2.threshold(frame1,200,255,0)
    #frame1 = cv2.Canny(frame1, 125, 280)
    
    
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()