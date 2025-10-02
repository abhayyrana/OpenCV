""" Document Detection and Perception Functions """

import cv2
import numpy as np
from OCR import min_document_area

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)
    return edged

def find_doc_contour(edged):
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for contour in contours[:5]:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02*perimeter, True)

        if len(approx) == 4:
            area = cv2.contourArea(approx)
            if area > min_document_area:
                return approx
    return None

def order_points(points):
    points = points.reshape(4, 2)
    ordered_points = np.zeros((4, 2), dtype=np.float32)

    # top-left point has smallest sum, and bottom-right point has largest sum
    point_sum = np.sum(points, axis=1)
    ordered_points[0] = points[np.argmin(point_sum)]
    ordered_points[2] = points[np.argmax(point_sum)]

    # top-right point has smallest difference, and bottom-left point has largest difference
    point_diff = np.diff(points, axis=1)
    ordered_points[1] = points[np.argmin(point_diff)]
    ordered_points[3] = points[np.argmax(point_diff)]

    return ordered_points

def tilt_transfrom(image, points):
    # transforming a tilted/angled document into a straighr, top-down view
    rect = order_points(points)
    (tl, tr, br, bl) = rect
    # calculating width and height of the new image
    width_top = np.sqrt(((tr[0] - tl[0])**2) +  ((tr[0] - tl[0])**2))
    width_bottom = np.sqrt(((br[0] - bl[0])**2) +  ((br[0] - bl[0])**2))
    max_width = int(max(width_top, width_bottom))
    height_left = np.sqrt(((tl[1] - bl[1])**2) +  ((tl[1] - bl[1])**2))
    height_right = np.sqrt(((tr[1] - br[1])**2) +  ((tr[1] - br[1])**2))
    max_height = int(max(height_left, height_right))

    # forming a perfect rectabgle
    desti = np.array([
        [0, 0],
        [max_width -1, 0],
        [max_width -1, max_height -1],
        [0, max_height -1]
    ], dtype=np.float32)

    M = cv2.getPerspectiveTransform(rect, desti)
    warped = cv2.warpPerspective(image, M, (max_width, max_height))
    return warped
