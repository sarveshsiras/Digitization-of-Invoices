import api_result
import table_processing
import cell_extraction
import output_cell_grouping
import numpy as np
import urllib
import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def get_table_coordinates_interface(URL):
	returned_coordinates = api_result.get_table(URL)
	return returned_coordinates

def crop_image_interface(URL, returned_coordinates):
	detected_table = api_result.crop_image(URL, returned_coordinates)
	return detected_table

def non_tabular_data_interface(URL, returned_coordinates):
	no_table_img = api_result.get_image(URL,returned_coordinates)
	print('--- Non-Tabular-Data ---')
	text = pytesseract.image_to_string(no_table_img, config="--oem 1 --psm 4")
	non_tabular_text = text
	return non_tabular_text

def table_processing_interface(detected_table):
	table_image = detected_table.copy()
	processed_img, border_image = table_processing.pre_process_table(detected_table)
	contours = table_processing.get_contours(processed_img,detected_table)
	contours.sort(key=lambda x: table_processing.get_contour_precedence(x,processed_img.shape[1]))
	bounding_rects = cell_extraction.get_text(contours)
	cell_images_rows = output_cell_grouping.group_output(bounding_rects, table_image)
	text_data = output_cell_grouping.process_text(cell_images_rows)
	print("--- Grouped Tabular Information ---")
	print(text_data)
	return text_data





