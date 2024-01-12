import numpy as np
import cv2

cap = cv2.VideoCapture(0)

lower = np.array([0, 100, 100])
upper = np.array([40, 255, 255])

mode = ''

while True:
    ret, img = cap.read()
    if not ret: break

    if mode == 'hsv':
        img_h = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_t = cv2.inRange(img_h, lower, upper)
    else:
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, img_t = cv2.threshold(img_g, 127, 255, cv2.THRESH_BINARY_INV)

    cont_list, hierachy = cv2.findContours(img_t,
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    img_f = cv2.drawContours(img, cont_list, -1, (250, 180, 180), 5)

    cv2.imshow('win', img)

    key = cv2.waitKey(1)
    if key == 27: break

cap.release()
cv2.destroyAllWindows()
