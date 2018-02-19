import cv2


cap = cv2.VideoCapture("dataset/examples-video/test.mp4")
#ret, frame = cap.read()


while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #ret, frame1 = cv2.threshold(frame1,0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #frame1 = cv2.morphologyEx(frame1, cv2.MORPH_CLOSE, kernel)
    ret, frame1 = cv2.threshold(frame1,100,255,0)
    frame1, contours, hierarchy = cv2.findContours(frame1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()