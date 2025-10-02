# IMAGE TRANSFORMATION AND MANIPULATION

import cv2
import numpy as np

# load an image from file
image1 = cv2.imread('Uploadd_Images\Cat Image jpg.jpg')
''' Copy the relative path to the image file '''

cv2.imshow('Cat Image', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resizing and scaling an image
resize = cv2.resize(image1, (800, 600))
''' syntax: cv2.resize(source, (width, height), fx, fy, interpolation) '''
cv2.imshow('resized Cat Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cropping an image using slicing
cropped = resize[150:500, 250:650]
''' syntax: image[startY:endY, startX:endX] '''
cv2.imshow('cropped Cat Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image rotation
(h, w) = resize.shape[:2]
''' if idhar (h, w) liya hai then, warpAffine mein (w, h) hi dena hai '''
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(resize, M, (w, h))

cv2.imshow('rotated Cat Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image flipping
flipped_h = cv2.flip(resize, 1)
flipped_v = cv2.flip(resize, 0)
flipped_b = cv2.flip(resize, -1)
''' 0 for vertical flip, 1 for horizontal flip, -1 for both '''
cv2.imshow('horizontal flip', flipped_h)
cv2.imshow('vertical flip', flipped_v)
cv2.imshow('both flip', flipped_b)
cv2.waitKey(0)
cv2.destroyAllWindows()
