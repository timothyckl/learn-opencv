import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    width, height = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), \
            int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    
    mid_width = int(width / 2)
    mid_height = int(height / 2)

    # line from top left to bottom right
    img = cv.line(img=frame, pt1=(0, 0), pt2=(width, height), \
            color=(255, 0, 0), thickness=5)
    # line from top right to bottom left
    img = cv.line(img=img, pt1=(0, height), pt2=(width, 0), \
            color=(0, 0, 255), thickness=5)
    # line from middle left to middle right
    img = cv.line(img=img, pt1=(0, mid_height), pt2=(width, mid_height), \
            color=(0, 255, 0), thickness=5)
    # line from middle top to middle bottom
    img = cv.line(img=img, pt1=(mid_width, 0), pt2=(mid_width, height), \
            color=(0, 255, 255), thickness=5)

    # rectangle
    img = cv.rectangle(img=img, pt1=(mid_width - 500, mid_height - 50), \
            pt2=(mid_width + 500, mid_height + 50), \
            color=(255, 105, 180), thickness=5)

    # circle
    img = cv.circle(img=img, center=(mid_width, mid_height), \
            radius=100, color=(255, 255, 0), thickness=-1)

    # text 
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.putText(img=img, text='!!!lao gan ma!!!', org=(mid_width - 500, \
            mid_height - 100), fontFace=font, fontScale=3, \
            color=(255, 255, 255), thickness=5, lineType=cv.LINE_AA)
        

    cv.imshow('frame', img)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
