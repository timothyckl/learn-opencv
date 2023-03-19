import cv2 as cv

img = cv.imread('./assets/cat.jpeg', -1)
# print(img.shape)

subset = img[500:1000, 500:1000]
img[1000:1500, 1000:1500] = subset

cv.imshow('subset', img)
cv.waitKey(0)
cv.destroyAllWindows()
