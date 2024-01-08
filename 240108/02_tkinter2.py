from tkinter import *
import os

def click():
    global DATA_PATH, IMG_LIST, IND
    IND += 1
    img_path = os.path.join(DATA_PATH, IMG_LIST[IND%len(IMG_LIST)])
    img.config(file = img_path)

if __name__=='__main__':
    DATA_PATH = "C:/Users/user/Desktop/img/1"
    IMG_LIST = ['1.png', '2.png', '3.png', '4.png']
    IND = 0

    main = Tk()

    img_path = os.path.join(DATA_PATH, '1.png')
    img = PhotoImage(file=img_path)

    lal = Label(main, image=img)
    lal.pack()

    bnt = Button(main, text='button', command=click)
    bnt.pack()

    main.mainloop()
