import numpy as np
import cv2

#trackbar
def nothing(x):
    pass

def trackbar_demo():
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('img')

    cv2.createTrackbar('R', 'img', 0, 255, nothing)
    cv2.createTrackbar('G', 'img', 0, 255, nothing)
    cv2.createTrackbar('B', 'img', 0, 255, nothing)

    switch = '0:OFF\n1:ON'
    cv2.createTrackbar(switch, 'img', 1, 1, nothing)

    while True:
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        r = cv2.getTrackbarPos('R', 'img')
        g = cv2.getTrackbarPos('G', 'img')
        b = cv2.getTrackbarPos('B', 'img')
        s = cv2.getTrackbarPos(switch, 'img')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]

    cv2.destroyAllWindows()

#trackbar_demo()

def add_scalar():
    src = cv2.imread('../image/cat.jpg', cv2.IMREAD_COLOR)
    dts1 = cv2.add(src, 100)
    dts2 = cv2.add(src, (100, 100, 100, 0))

    cv2.imshow('win1', dts1)
    cv2.imshow('win2', dts2)
    cv2.waitKey()
    cv2.destroyAllWindows()

#add_scalar()

#overlay
def create_custom_trackbar(name, win_name, value, max_value, userdata):
    def callback(value):
        img1 = userdata[0]
        img2 = userdata[1]

        alpha = value/100
        dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
        cv2.imshow('win', dst)

    cv2.createTrackbar(name, win_name, value, max_value, callback)

def overlay():
    img1 = cv2.imread('../image/cloud.jpg')
    img2 = cv2.imread('../image/london.jpg')

    h, w, _ = img1.shape
    img2 = cv2.resize(img2, dsize=(w, h), interpolation=cv2.INTER_AREA)

    cv2.imshow('win', img1)
    create_custom_trackbar('fade', 'win', 0, 100, [img1, img2])

    cv2.waitKey()
    cv2.destroyAllWindows()

#overlay()
