import numpy as np
import cv2 as cv

img = cv.imread('./assets/cat.jpeg')
# print(img.shape)

# harris corner detection
def harris_corner_detection(image):  
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # convert to grascale
    gray_float = gray.astype(np.float32)  # convert to float32
    # harris corner detection algorithm
    # blockSize: neighbourhood size
    # ksize: aperture parameter
    # k: Harris detector free parameter in the equation (R = det(M) - k(trace(M))^2
    result = cv.cornerHarris(src=gray_float, blockSize=3, ksize=3, k=0.04) 
    result = cv.dilate(result, None)  # dilate the corner points
    image[result > 0.01 * result.max()] = [0, 255, 0]

    return image

# shi-tomasi corner detection
def shi_tomasi_corner_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # convert to grayscale
    gray_float = gray.astype(np.float32)  # convert to float32
    # Shi-Tomasi corner detection algorithm
    corners = cv.goodFeaturesToTrack(
        image=gray_float, maxCorners=1000, qualityLevel=0.01, minDistance=10)
    corners = corners.astype(np.int32)  # convert to int32

    for coordinate in corners:
        x, y = coordinate.ravel()
        cv.circle(image, center=(x,y), radius=5, color=[255, 0, 0], \
                thickness=-1)

    return image

cv.imshow('shi-tomasi', shi_tomasi_corner_detection(img))
# cv.imshow('harris', harris_corner_detection(img))
cv.waitKey(0)
cv.destroyAllWindows()
