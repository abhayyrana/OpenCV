# BASIC IMAGE DRAWING TECHNIQUES

import cv2
import numpy as np

image1 = cv2.imread('Uploadd_Images\Cat Image jpg.jpg')
resize = cv2.resize(image1, (800, 600))
cv2.imshow('Cat Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# drawing a line
cv2.line(resize, (225, 50), (700, 500), (0, 0, 255), 5)
cv2.line(resize, (225, 500), (700, 50), (0, 0, 255), 5)
''' syntax: cv2.line(image, start_point, end_point, color, thickness) '''
cv2.imshow('Line on Cat Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# drawing a rectangle
cv2.rectangle(resize, (225, 50), (700, 500), (0, 255, 0), 5)
''' syntax: cv2.rectangle(image, top_left_point, bottom_right_point, color, thickness) 
    If thickness is -1, it fills the rectangle '''
cv2.imshow('Rectangle on Cat Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# drawing a circle
cv2.circle(resize, (465, 410), 50, (255, 0, 0), 5)
''' syntax: cv2.circle(image, center, radius, color, thickness) '''
cv2.imshow('Circle on Cat Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# adding text on picture
text = cv2.putText(resize, 'Cute cat', (220, 530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
''' syntax: cv2.putText(image, text, bottom_left_pt, font, font_scale, color, thickness) '''
cv2.imshow('Text on Cat Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
