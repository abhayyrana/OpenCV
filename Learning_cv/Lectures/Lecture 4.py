# IMAGE FILTERING AND BLURRING

import cv2
import numpy as np

image1 = cv2.imread(r'Learning_cv\Uploaded_Images\Cat Image jpg.jpg')
resize = cv2.resize(image1, (600, 400))


# gaussian blur
blurred = cv2.GaussianBlur(resize, (7, 7), 0)
''' syntax: cv2.GaussianBlur(image, (kernel_width_x, kernel_height_y), sigma)
    kernel size must be odd and positive, sigma can be 0 for automatic calculation '''

# median blur
median_blur = cv2.medianBlur(resize, 5)
''' syntax: cv2.medianBlur(image, kernel_size)
    kernel size must be odd and positive '''

# sharpening
kernel = np.array([[0, -1, 0],
                         [-1, 5, -1],
                         [0, -1, 0]])
''' syntax: np.array([[...], [...], [...]]) for defining a kernel matrix for sharpening '''
kernel = kernel.astype(np.float32)
''' ensure the kernel is in float32 format '''
sharpened_im = cv2.filter2D(resize, -1, kernel)
''' syntax: cv2.filter2D(image, -1, kernel) 
    -1 means same depth as input image, kernel is a numpy array for sharpening '''

cv2.imshow('Cat Image', resize)
cv2.imshow('Gaussian Blur on Cat Image', blurred)
cv2.imshow('Median Blur on Cat Image', median_blur)
cv2.imshow('Sharpened Cat Image', sharpened_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
