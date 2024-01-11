import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)

lower_hue = np.array([0, 100, 100])
upper_hue = np.array([40, 255, 255])
while True:
    ret, img = cap.read()
    if not ret: break

    cv2.imshow('win1', img)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', img_hsv)
    img_mask = cv2.inRange(img_hsv, lower_hue, upper_hue)
    cv2.imshow('win2', img_mask)
    key = cv2.waitKey(1)
    if key == 27: break
    

cap.release()
cv2.destroyAllWindows()
