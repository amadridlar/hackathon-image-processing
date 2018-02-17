import cv2

cap = cv2.VideoCapture("dataset/examples-video/test.mp4")
# ret, frame = cap.read()

while (cap.isOpened()):
    ret, frame = cap.read()
    #frame = cv2.subtract(frame1, frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 2)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
