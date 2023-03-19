import numpy as np
import cv2 as cv

capture = cv.VideoCapture(1)  # our webcam is located at index 1

while True:
    ret, frame = capture.read()
    width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    img = np.zeros(frame.shape, np.uint8)
    # resize both axes of the frame to 1/2 of its size so
    # we can fit 4 of them in the image
    small_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # top left
    img[:height//2, :width//2] = cv.rotate(small_frame, cv.ROTATE_180)   
    # bottom left
    img[height//2:, :width//2] = np.expand_dims(
            cv.cvtColor(small_frame, cv.COLOR_BGR2GRAY), 
            axis=2)
    # top right
    img[:height//2, width//2:] = np.expand_dims(
            cv.cvtColor(
                cv.rotate(small_frame, cv.ROTATE_180), cv.COLOR_BGR2GRAY), 
            axis=2)
    # bottom right
    img[height//2:, width//2:] = small_frame

    cv.imshow('frame', img)

    # will wait for 1 ms for the 'q' key to be pressed
    # else it will continue to the next iteration
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()


