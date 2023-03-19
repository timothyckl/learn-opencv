import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    width, height = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), \
            int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    mid_width = int(width / 2)
    mid_height = int(height / 2)

    hsv = cv.cvtColor(src=frame, code=cv.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv.inRange(src=hsv, lowerb=lower_blue, upperb=upper_blue)
    res = cv.bitwise_and(src1=frame, src2=frame, mask=mask)

    cv.imshow('mask', mask)
    cv.imshow('result', res)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
