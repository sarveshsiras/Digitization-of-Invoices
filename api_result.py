import numpy as np
import cv2
from PIL import Image
from server_request import dispatch_request

def get_table(img_path):
    returned_coordinates = dispatch_request("NGROK_URL", img_path)
    print(returned_coordinates)
    img = Image.open(img_path)
    cropped_image = img.crop(returned_coordinates)
    open_cv_image = np.array(cropped_image)
    # Convert RGB to BGR
    # open_cv_image = open_cv_image[:, :, ::-1].copy()
    #open_cv_image = cv2.imread(img_path)
    return open_cv_image,returned_coordinates

def get_image(img_path,returned_coordinates):
    x1_coordinate = int(returned_coordinates[0])
    y1_coordinate = int(returned_coordinates[1])
    x2_coordinate = int(returned_coordinates[2])
    y2_coordinate = int(returned_coordinates[3])
    img = cv2.imread(img_path)
    img[y1_coordinate:y2_coordinate, x1_coordinate:x2_coordinate] = [255,255,255]
    cv2.imwrite("Cropped_invoice.png",img)
    return img


