# formacion10.py
import numpy as np
import cv2

cap = cv2.VideoCapture("dataset/examples-video/test.mp4")

# face_cascade = cv2.CascadeClassifier('libraries/data/haarcascades/cascadeH5.xml')
face_cascade = cv2.CascadeClassifier('libraries/data/haarcascades/HS.xml')
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    height = np.size(frame, 0)
    width = np.size(frame, 1)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        img_rect = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow('frame',img_rect if len(faces) > 1 else frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
