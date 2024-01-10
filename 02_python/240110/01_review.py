import numpy as np
import cv2
import os

def load_color_and_gray_img(path):
    global IMG_WIDTH, IMG_HEIGHT

    img_c = cv2.imread(path, cv2.IMREAD_COLOR)
    img_g = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img_g = cv2.cvtColor(img_g, cv2.COLOR_GRAY2BGR)

    img_c = cv2.resize(img_c, dsize=(IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_LINEAR)
    img_g = cv2.resize(img_g, dsize=(IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_LINEAR)

    return img_c, img_g

if __name__=='__main__':
    IMG_WIDTH = 300
    IMG_HEIGHT = 200

    IMG_PATH = '../image'
    IMG_FILES = ['cat.jpg', 'cloud.jpg', 'london.jpg']

    imgs = list()
    for name in IMG_FILES:
        img_path = os.path.join(IMG_PATH, name)
        img_c, img_g = load_color_and_gray_img(img_path)

        imgs.append(np.concatenate((img_c, img_g), axis=1))

    ret = np.concatenate(imgs, axis=0)

    cv2.imshow('ret', ret)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
