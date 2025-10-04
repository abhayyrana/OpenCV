# WORKING WITH VIDEO AND WEBCAM

import cv2
import numpy as np

# video capture from webcam
cap = cv2.VideoCapture(0)
''' 0 for built-in webcam, 1 for external webcam, 2 for virtual webcam '''
while True:
    ret, frame = cap.read() # ret = True/False, frame = image from webcam
    if not ret:
        print("Could not read frame")
        break
    cv2.imshow('Webcam Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to exit
        print("Exiting...")
        break
cap.release() # release the webcam
cv2.destroyAllWindows()

# saving webcam video to file in openCV
camera = cv2.VideoCapture(0)
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
comp_format = cv2.VideoWriter_fourcc(*'XVID') # compression format
recorder = cv2.VideoWriter('Webcam_Video.avi', comp_format, 20.0, (frame_width, frame_height))
''' syntax: cv2.VideoWriter(filename, compression_format(fourcc), fps, frame_size(w, h)) '''
while True:
    ret, frame = camera.read()
    if not ret:
        print("Could not read frame")
        break
    recorder.write(frame) # write the frame to the video file
    cv2.imshow('Recording live', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting and saving video...")
        break
camera.release() # release the webcam
recorder.release() # release the video writer
cv2.destroyAllWindows()
