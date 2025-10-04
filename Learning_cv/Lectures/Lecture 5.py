# EDGE DETECTION AND THRESHOLDING

import cv2
import numpy as np

image1 = cv2.imread('Uploaded_Images\Cat Image jpg.jpg', cv2.IMREAD_GRAYSCALE)
resize = cv2.resize(image1, (600, 400))

# canny edge detection
edges = cv2.Canny(resize, 50, 150)
''' syntax: cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None) 
    threshold1: first threshold for the hysteresis procedure
    threshold2: second threshold for the hysteresis procedure. '''
cv2.imshow('Original Image', resize)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# thresholding
ret, threshold_img = cv2.threshold(resize, 100, 255, cv2.THRESH_BINARY)
''' syntax: cv2.threshold(source, thresh_val, max_val, type, dst=None) 
    source: input image
    thresh_val: threshold value
    max_val: maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types
    type: thresholding type
    dst: output image (optional) '''
cv2.imshow('Original Image', resize)
cv2.imshow('Thresholded Image', threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# bitwise operations
''' 1- cv2.bitwise_and(img1, img2, dst=None, mask=None)
    2- cv2.bitwise_or(img1, img2, dst=None, mask=None)
    3- cv2.bitwise_not(src, dst=None, mask=None)
    4- cv2.bitwise_xor(img1, img2, dst=None, mask=None) 
    
    * img1 and img2 must be of the same size and type
    ** use only black and white images for bitwise operations '''
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

cv2.circle(img1, (150, 150), 100, (225, 0, 0), -1)
cv2.rectangle(img2, (50, 50), (200, 200), (225, 0, 0), -1)

b_and = cv2.bitwise_and(img1, img2)
b_or = cv2.bitwise_or(img1, img2)
b_not = cv2.bitwise_not(img1)
b_xor = cv2.bitwise_xor(img1, img2)

cv2.imshow('circle', img1)
cv2.imshow('rectangle', img2)
cv2.imshow('bitwise_and', b_and)
cv2.imshow('bitwise_or', b_or)
cv2.imshow('bitwise_not', b_not)
cv2.imshow('bitwise_xor', b_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
