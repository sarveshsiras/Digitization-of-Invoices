
import api_result
import table_processing
import text_extraction
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


image_path = "../input_imgs/org_invoice.png"

detected_table,returned_coordinates = api_result.get_table(image_path)
no_table_img = api_result.get_image(image_path,returned_coordinates)

# -----------------------------------------------------------------------------------------------
# For Table Processing
#img_processed = preprocessing.remove_noise_and_smooth(detected_table)
processed_img, border_image = table_processing.pre_process_table(detected_table)
contours = table_processing.get_contours(processed_img,detected_table)
contours.sort(key=lambda x: table_processing.get_contour_precedence(x,processed_img.shape[1]))
rectangle_list,text_data = text_extraction.get_text(contours,border_image)
print(text_data)
# ---------------------------------------------------------------------------------------------------------

text = pytesseract.image_to_string(no_table_img, config="--oem 1 --psm 4")
print(text)