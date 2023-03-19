import cv2 as cv

# check version
# print(cv.__version__)

img = cv.imread('./assets/cat.jpeg', 0)
print('before: ', type(img), img.shape, img.size)

img = cv.resize(img, (0, 0), fx=.5, fy=.5)  # shrink xy by factor of 1/2
print('resized: ', type(img), img.shape, img.size)


rotation_options = [
        cv.ROTATE_90_CLOCKWISE,  # 90 deg clockwise
        cv.ROTATE_180,  # 180 def clockwise
        cv.ROTATE_90_COUNTERCLOCKWISE
        ]

img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
print('rotate: ', type(img), img.shape, img.size)

cv.imwrite('./assets/new_image.jpg', img)
cv.imshow('cat', img)
cv.waitKey(0)
cv.destroyAllWindows()




