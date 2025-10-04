# BASICS OF CV AND IMAGE FUNCTIONS

import cv2
import numpy as np

# load an image from file
image1 = cv2.imread('Uploaded_Images\Cat Image png.png')
''' Copy the relative path to the image file '''

if image1 is None:
    print("Error: Could not read the image.")
else:
    print("Image loaded successfully.")

# display the image in a window
cv2.imshow('Cat Image', image1)
cv2.waitKey(0)
''' 0 means wait indefinitely until a key is pressed
    1 means wait for 1 millisecond
    2 means wait for 2 milliseconds, etc. '''
cv2.destroyAllWindows()

# save the image to a new file
cv2.imwrite('Cat Image copy.png', image1)

# image dimensions
height, width, channels = image1.shape
''' Channels 3 means the image is in RGB format
    channels 2 means the image is in BGR format
    Channels 1 means the image is in grayscale format
    No channels means the image is empty '''
print(f"Image dimensions: {width}x{height}, Channels: {channels}")

# convert the image to grayscale
grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cat Image Grey', grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
