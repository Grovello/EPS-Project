# --------------------------------

import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while True:
    """Take the frame from video stream"""
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    """Haar Cascade function for face recognition"""
    face_cascade = cv2.CascadeClassifier("D:\Python img\haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("D:\Python img\haarcascade_eye.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 50)

    """Rectangle of face and ROI creation"""
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        """Rectangle of eyes creation"""
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 15)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)

    cv2.imshow("My Camera", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
