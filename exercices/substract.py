import cv2
import numpy as np

cap = cv2.VideoCapture("../dataset/examples-video/test.mp4")
kernel = np.ones((3, 3), np.uint8)
ret, bkFrame = cap.read()
bkFrame = cv2.cvtColor(bkFrame, cv2.COLOR_BGR2GRAY)
bkFrame = cv2.morphologyEx(bkFrame, cv2.MORPH_CLOSE, kernel)
#fgbg = cv2.createBackgroundSubtractorMOG2()


while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame1  = cv2.morphologyEx(frame1, cv2.MORPH_CLOSE,kernel)
    #frame1 = cv2.adaptiveThreshold(frame1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    frame1 = cv2.subtract(frame1, bkFrame)
    frame1 = cv2.Canny(frame1, 30, 70)
    #frame1 = cv2.morphologyEx(frame1, cv2.MORPH_OPEN, kernel)
    #frame1 = fgbg.apply(frame1)
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()