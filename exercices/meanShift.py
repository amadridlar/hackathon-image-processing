import cv2
import numpy as np


cap = cv2.VideoCapture("../dataset/examples-video/test.mp4")
ret, frame1 = cap.read()

# Configuracion de la ubicacion inicial de la ventana
r, h, c, w = 457, 100, 306, 100  # simply hardcoded the values
track_window = (c, r, w, h)

# establece el ROI para rastrear
roi = frame1[r:r + h, c:c + w]
hsv_roi = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Configure el criterio de terminacion, ya sea 10 iteracion o mover por lo menos 1 pt.
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 50, 1)




while (cap.isOpened()):
    ret, frame1 = cap.read()
    frame1 = cv2.resize(frame1, (0, 0), fx=0.5, fy=0.5)
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #ret, frame1 = cv2.threshold(frame1,0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #frame1 = cv2.morphologyEx(frame1, cv2.MORPH_CLOSE, kernel)
    ret, frame1 = cv2.threshold(frame1,100,255,0)
    frame1, contours, hierarchy = cv2.findContours(frame1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([frame1], [0], roi_hist, [0, 180], 1)

    # Aplica meanshift para conseguir la nueva ubicacion.
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

    # Dibujalo en la imagen
    x, y, w, h = track_window
    img2 = cv2.rectangle(frame1, (x, y), (x + w, y + h), 255, 2)

    
    
    
    
    

    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()