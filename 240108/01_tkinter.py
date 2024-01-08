from tkinter import *

def click():
    if but.cget('background') == 'Green':
        but.configure(text='off', background='Red')
    else:
        but.configure(text='on', background='Green')

main = Tk()
screen_w = main.winfo_screenwidth()
screen_h = main.winfo_screenheight()

main.title("Tk")
main.geometry(f"{screen_w}x{screen_h}")
main.resizable(width=False, height=True)

lbl = Label(main)
lbl['text'] = 'click plz'
lbl['font'] = 'Arial 20'

lbl.pack()

but = Button(main, text="on", background="Green", command=click)
but.pack()

main.mainloop()
