import numpy as np
import cv2

cap = cv2.VideoCapture(0)

lower1 = np.array([0, 100, 100])
upper1 = np.array([20, 255, 255])
lower2 = np.array([160, 100, 100])
upper2 = np.array([180, 255, 255])

mode = ''

while True:
    ret, img = cap.read()
    if not ret: break

    if mode == 'hsv':
        img_h = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_t = cv2.inRange(img_h, lower1, upper1) + cv2.inRange(img_h, lower2, upper2) 
    else:
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, img_t = cv2.threshold(img_g, 127, 255, cv2.THRESH_BINARY_INV)

    cont_list, hierachy = cv2.findContours(img_t,
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    
    areas = [cv2.contourArea(c) for c in cont_list]
    max_ind = areas.index(max(areas))
    max_cont = cont_list[max_ind]

    img_f = cv2.drawContours(img, max_cont, -1, (210, 180, 200), 3)

    cnt = cont_list[0]
    M = cv2.moments(cnt)
    if M['m00']:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print(cx, cy)
        cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)

    cv2.imshow('win', img)

    key = cv2.waitKey(1)
    if key == 27: break

cap.release()
cv2.destroyAllWindows()
