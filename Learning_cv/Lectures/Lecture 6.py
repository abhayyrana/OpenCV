# CONTOURS & SHAPE DETECTION

import cv2
import numpy as np

image1 = cv2.imread(r'Learning_cv\Uploaded_Images\Triangle.jpg')
resize = cv2.resize(image1, (400, 400))
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', resize)

# finding contours
_, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
''' syntax: cv2.findContours(image, mode, method, contours=None, hierarchy=None, offset=None) '''

# draw contours
cv2.drawContours(resize, contours, -1, (0, 0, 255), 2)
''' syntax: cv2.drawContours(image, contours, contour_idx, color, thickness)
    contour_index=> -1 to draw all contours
                    0 to draw first contour
                    1 to draw second contour
                    2 to draw third contour
                    ...'''
cv2.imshow('Contours', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# contour shape detection
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    ''' syntax: cv2.approxPolyDP(curve, epsilon(0.01 * arc_length), closed) '''
    corner = len(approx)
    if corner == 3:
        shape_name = "triangle"
    elif corner == 4:
        shape_name = "quadrilateral"
    elif corner == 5:
        shape_name = "pentagon"
    elif corner > 5:
        shape_name = "circle"
    else:
        shape_name = "unknown"

    cv2.drawContours(resize, [approx], 0, (0, 0, 255))
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(resize, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv2.imshow('Contours', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
