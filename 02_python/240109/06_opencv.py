import cv2
import numpy as np

print(cv2.__version__)

img_file = cv2.imread('../image/cat.jpg')
"""
#basic
cv2.imshow('title', img_file)
cv2.waitKey()
cv2.destroyAllWindows()

#channel
img = np.zeros((300, 400, 3), np.uint8)
img[:,:] = (200, 200, 250) #(B, G, R)

cv2.imshow('window title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#multi window
cv2.imshow('1', img_file)
cv2.imshow('2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

cat1 = cv2.imread('../image/cat.jpg', cv2.IMREAD_COLOR)
cat2 = cv2.imread('../image/cat.jpg', cv2.IMREAD_GRAYSCALE)

"""
#color and gray
cv2.imshow('color', cat1)
cv2.imshow('gray', cat2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cat3 = cv2.cvtColor(cat2, cv2.COLOR_GRAY2BGR)
cat_stack = np.hstack((cat1, cat3))
#cat_stack = np.concatenate((cat1, cat3), axis=1)

cv2.imshow('stack', cat_stack)
cv2.waitKey(0)
cv2.destroyAllWindows()

#save
cv2.imshow('win', img_file)
key = cv2.waitKey(0)
if key == 27:
    cv2.imwrite('cat_2.jpg', img_file)
cv2.destroyAllWindows()
"""
