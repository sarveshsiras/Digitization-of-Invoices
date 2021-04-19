
import api_result
import table_processing
import cell_extraction
import output_cell_grouping
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


image_path = "new_invoice.jpeg"

detected_table,returned_coordinates = api_result.get_table(image_path)
table_image = detected_table.copy()
no_table_img = api_result.get_image(image_path,returned_coordinates)

# -----------------------------------------------------------------------------------------------
# For Table Processing
processed_img, border_image = table_processing.pre_process_table(detected_table)
contours = table_processing.get_contours(processed_img,detected_table)
contours.sort(key=lambda x: table_processing.get_contour_precedence(x,processed_img.shape[1]))
bounding_rects = cell_extraction.get_text(contours)
cell_images_rows = output_cell_grouping.group_output(bounding_rects, table_image)
text_data = output_cell_grouping.process_text(cell_images_rows)
print("--- Grouped Tabular Information ---")
print(text_data)


# ---------------------------------------------------------------------------------------------------------
print('--- Non-Tabular-Data ---')
text = pytesseract.image_to_string(no_table_img, config="--oem 1 --psm 4")
print(repr(text))
result_text = text.split("\n")
print(result_text)
