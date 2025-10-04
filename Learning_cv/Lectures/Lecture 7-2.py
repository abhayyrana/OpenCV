# USING FACE, EYE & SMILE CASCADES

import cv2
import numpy as np

face = cv2.CascadeClassifier(r"Learning_cv\Haar Cascades\haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier(r"Learning_cv\Haar Cascades\haarcascade_eye.xml")
smile = cv2.CascadeClassifier(r"Learning_cv\Haar Cascades\haarcascade_smile.xml")

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # roi - region of interest.
        roi_gray = gray[y:y+h, x:x+h]
        roi_color = frame[y:y+h, x:x+h]
        ''' This function basically eleminates all the remaining area except the face,
            so that it is easier to find the eyes and smile, which are in the face only. '''
        eyes = eye.detectMultiScale(roi_gray, 1.1, 5)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        smiles = smile.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smile Detected", (x, y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow("Smart Face Detector.", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()