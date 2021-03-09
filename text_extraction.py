import cv2
import pytesseract


def get_text(contours,border_image):
    rectangle_list = []
    text_data = []
    plot_num = 1
    for j in range(len(contours)):
        peri = cv2.arcLength(contours[j], True)
        approx = cv2.approxPolyDP(contours[j], 0.01 * peri, True)
        if (len(approx) == 4):
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            l = [[x, y], [x+w, y+h]]
            rectangle_list.append(l)
            # print(aspectRatio)
            cv2.rectangle(border_image, (x, y), (x + w, y + h), (0, 0, 0), 1)
            rect_img = border_image[y:y + h, x:x + w]
            # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
            # border = cv2.copyMakeBorder(rect_img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255])
            # resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            # dilation = cv2.dilate(resizing, kernel, iterations=1)
            # erosion = cv2.erode(dilation, kernel, iterations=1)
            # cv2.putText(image, "RECT", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            text = pytesseract.image_to_string(rect_img, config="--oem 1 --psm 6")
            if len(text) == 1:
                text = pytesseract.image_to_string(rect_img, config="--oem 1 --psm 4")
                print("-----------------INSIDE------------------")

            print(text)
            # print(l)
            #print("---------------------------------------------")
            text_data.append(text)
            cv2.imshow("RESULT", border_image)
            cv2.waitKey(0)
            # fig.add_subplot(rows, columns, plot_num)
            plot_num = plot_num + 1
            # plt.imshow(rect_img)
            # plt.axis('off')

    # plt.show()
    print(plot_num)
    print(rectangle_list)
    return rectangle_list,text_data

