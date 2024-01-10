import cv2
import matplotlib.pyplot as plt

# opencv to matplotlib
def opencv_to_matplotlib():
    img = cv2.imread('../image/cat.jpg', cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()

# camera
import sys

def set_camera(cap):
    if not cap.isOpened():
        print("camera open failed")
        sys.exit()

    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

def show_frame(cap, flip=1, gray=False):
    
    set_camera(cap)

    while True:
        #read
        ret, img = cap.read()
        if not ret:
            print("can not read frame")
            break

        #transformation
        img = cv2.flip(img, flip)
        if gray:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #show
        cv2.imshow('win', img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def save_video(cap):
    set_camera(cap)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('video.avi', fourcc, 25.0, (320, 240))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('frame', frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

device = 0
cap = cv2.VideoCapture(device)
show_frame(cap)

cap = cv2.VideoCapture('../image/video.mp4')
#show_frame(cap, gray=True)
#save_video(cap)

