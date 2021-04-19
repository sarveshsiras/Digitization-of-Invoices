import cv2
import pytesseract


def get_text(contours):
    rectangle_list = []
    for j in range(len(contours)):
        peri = cv2.arcLength(contours[j], True)
        approx = cv2.approxPolyDP(contours[j], 0.01 * peri, True)
        if (len(approx) == 4):
            x, y, w, h = cv2.boundingRect(approx)
            rectangle_list.append((x, y, w, h))

    return rectangle_list

