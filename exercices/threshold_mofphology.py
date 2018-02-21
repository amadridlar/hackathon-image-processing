import cv2
import numpy as np

cap = cv2.VideoCapture("dataset/examples-video/test.mp4")
kernel = np.ones((3, 3), np.uint8)
ret, frame = cap.read()


while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame1 = cv2.adaptiveThreshold(frame1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    #frame1 = cv2.morphologyEx(frame1, cv2.MORPH_OPEN, kernel)
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()