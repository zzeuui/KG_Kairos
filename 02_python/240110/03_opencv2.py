import numpy as np
import cv2

# figure
def figure():
    img = np.zeros((512, 512, 3), np.uint8)
    img = np.full((512, 512, 3), (255, 255, 255), np.uint8)
    img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    img = cv2.rectangle(img, (348, 0), (510, 128), (0, 255, 0), 3)
    img = cv2.circle(img, (200, 200), 25, (0, 0, 255), -1) #-1:fill, >0: solid

    pts = np.array([[10,5],[100,110],[170,120],[150,110]], np.int32)
    img = cv2.polylines(img, [pts], True, (0, 255, 255))

    cv2.imshow('win', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#figure()

#mouse event
def draw_circle(event, x, y, flags, param):
    img = param[0]

    color = [np.random.randint(0, 255) for _ in range(3)]
    size = np.random.randint(10, 100)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), size, color, -1)
        cv2.imshow('win', img)

def mouse_event():
    img = np.full((512, 512, 3), (255, 255, 255), np.uint8)
    cv2.namedWindow('win')
    cv2.setMouseCallback('win', draw_circle, param=[img])

    cv2.imshow('win', img)
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

#mouse_event()

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    img = param[0]

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (255,0,0), -1)
            else:
                cv2.circle(img, (x,y), 5,(0,255,0), -1)

if __name__=='__main__':
    drawing = False
    mode = True
    ix, iy = -1, -1
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('win')
    cv2.setMouseCallback('win', draw_circle, param=[img])

    while True:
        cv2.imshow('win', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'): mode = not mode
        elif k == ord('q'): break

    cv2.destroyAllWindows()
