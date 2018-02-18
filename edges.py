import cv2

cap = cv2.VideoCapture("dataset/examples-video/test.mp4")
#ret, frame = cap.read()


while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    ret, frame1 = cv2.threshold(frame1,0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #frame1 = cv2.morphologyEx(frame1, cv2.MORPH_CLOSE, kernel)
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()