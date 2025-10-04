# FACE & OBJECT DETECTION

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("Haar Cascades\haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    ''' detectMultiScale() - used to scan and detect faces.
        scaleFactor - zoom level to use to find a face.
        minNeighbors - how many neighbors each candidate rectangle should have to retain it.
        minNeighbor = 3 -> loose checking
                    = 5 -> safe checking
                    = 6 -> strict checking.'''
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        ''' x = how far from left
            y = how far from top
            w = width of the face
            h = height of the face

            (x, y) = top-left corner
            (x+w, y+h) = bottom-right corner
        '''
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()