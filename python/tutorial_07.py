import numpy as np
import cv2 as cv

image = cv.imread('./assets/cat.jpeg', cv.IMREAD_GRAYSCALE)
template = cv.imread('./assets/ears.png', cv.IMREAD_GRAYSCALE)
template_height, template_width = template.shape

methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, \
        cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for idx, method in enumerate(methods):
    img = image.copy()  # copy image for each method to avoid overwriting
    result = cv.matchTemplate(img, templ=template, method=method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    # print(min_val, max_val, min_loc, max_loc)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv.rectangle(img=img, pt1=top_left, pt2=bottom_right, \
            color=255, thickness=5)

    cv.imshow(winname=f'method {idx}', mat=img)
    cv.waitKey(delay=0)
    cv.destroyAllWindows()
