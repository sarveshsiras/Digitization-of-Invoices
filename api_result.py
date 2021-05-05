import numpy as np
import cv2
import s3_image_download
from PIL import Image
from server_request import dispatch_request

def get_table(img_path):
    print("Start the process")
    # returned_coordinates = [209.32167053222656, 445.782958984375, 757.7854614257812, 655.8165893554688]
    returned_coordinates = [275.050048828125, 510.5257873535156, 1332, 1557]
    # returned_coordinates = dispatch_request("http://7a43df8501c8.ngrok.io", img_path)
    print(returned_coordinates)
    # img = Image.open(img_path)
    #oimg = cv2.imread(img_path)
    oimg = s3_image_download.url_to_image(img_path)
    cv2.rectangle(oimg, (int(returned_coordinates[0]), int(returned_coordinates[1])), (int(returned_coordinates[2]), int(returned_coordinates[3])), (0, 255, 0), 3)
    # cv2.imshow('detected table', oimg)
    # cv2.waitKey()
    return returned_coordinates

def crop_image(img_url, returned_coordinates):
    #img = cv2.imread(img_url)
    img = s3_image_download.url_to_image(img_url)
    crop_img = img[round(float(returned_coordinates[1])):round(float(returned_coordinates[3])), round(float(returned_coordinates[0])):round(float(returned_coordinates[2]))]
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    return crop_img

def get_image(img_path,returned_coordinates):
    x1_coordinate = int(float(returned_coordinates[0]))
    y1_coordinate = int(float(returned_coordinates[1]))
    x2_coordinate = int(float(returned_coordinates[2]))
    y2_coordinate = int(float(returned_coordinates[3]))
    img = s3_image_download.url_to_image(img_path)
    img[y1_coordinate:y2_coordinate, x1_coordinate:x2_coordinate] = [255,255,255]
    return img


