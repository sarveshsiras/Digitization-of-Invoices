import cv2
import pytesseract

def cell_in_same_row(c1, c2):
    c1_center = c1[1] + c1[3] - c1[3] / 2
    c2_bottom = c2[1] + c2[3]
    c2_top = c2[1]
    return c2_top < c1_center < c2_bottom

def group_output(bounding_rects,image):
    print("Start grouping the rows")
    #print(type(bounding_rects[-1][0]))
    #print(bounding_rects[-1][0])
    if(bounding_rects[-1][0] == 0 and bounding_rects[-1][0] == 0):
        bounding_rects.pop()
    largest_rect = max(bounding_rects, key=lambda r: r[2] * r[3])
    #print(largest_rect)
    bounding_rects = [b for b in bounding_rects if b is not largest_rect]
    cells = [c for c in bounding_rects]
    orig_cells = [c for c in cells]
    rows = []
    while cells:
        first = cells[0]
        rest = cells[1:]
        cells_in_same_row = sorted(
            [
                c for c in rest
                if cell_in_same_row(c, first)
            ],
            key=lambda c: c[0]
        )

        row_cells = sorted([first] + cells_in_same_row, key=lambda c: c[0])
        rows.append(row_cells)
        cells = [
            c for c in rest
            if not cell_in_same_row(c, first)
        ]

    rows.sort(key=avg_height_of_center)
    cell_images_rows = []
    for row in rows:
        cell_images_row = []
        for x, y, w, h in row:
            cell_images_row.append(image[y:y + h, x:x + w])
        cell_images_rows.append(cell_images_row)
    return cell_images_rows

# Sort rows by average height of their center.
def avg_height_of_center(row):
    centers = [y + h - h / 2 for x, y, w, h in row]
    return sum(centers) / len(centers)

def get_text_data(img):
    return pytesseract.image_to_string(img, config="--psm 6")

def process_text(cell_images_rows):
    result_data = []
    for i in cell_images_rows:
        data_in_row = []
        for j in i:
            data_in_row.append(get_text_data(j))
        result_data.append(data_in_row)
    return result_data
