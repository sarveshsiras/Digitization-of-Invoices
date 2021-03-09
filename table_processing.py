import numpy as np
import cv2
import border
from PIL import Image

def pre_process_table(detected_table):
    image = border.get_border(detected_table)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh,image


def get_contours(thresh,detected_table):

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60, 1))
    detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
    cv2.imshow('result', detect_horizontal)
    cv2.waitKey()
    cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    print("Vertical", len(cnts))
    for c in cnts:
        cv2.drawContours(detected_table, [c], -1, (36, 255, 12), 2)

    # Detect vertical lines
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 10))
    detect_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    cv2.imshow('result', detect_vertical)
    cv2.waitKey()
    cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    print("horizantal", len(cnts))
    for c in cnts:
        cv2.drawContours(detected_table, [c], -1, (36, 255, 12), 2)

    cv2.imshow('Drawing_1', detected_table)
    cv2.waitKey()
    #cv2.imwrite("Detected_table.jpg",detected_table)

    img_vh = cv2.addWeighted(detect_vertical, 0.5, detect_horizontal, 0.5, 0.0)
    cv2.imshow('Drawing', img_vh)
    cv2.waitKey()

    contours, hierarchy = cv2.findContours(img_vh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    print(contours)
    return contours

def get_contour_precedence(contour, cols):
    tolerance_factor = 4
    origin = cv2.boundingRect(contour)
    return (((origin[1] + origin[3]) / 2 // tolerance_factor) * tolerance_factor) * cols + (origin[0] + origin[2]) / 2
