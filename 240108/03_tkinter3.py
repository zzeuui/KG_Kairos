import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #define
        self.num1 = tk.Entry(self, width=30)
        self.num2 = tk.Entry(self, width=30)

        buttons = [('+', self.add), ('-', self.sub),
                   ('*', self.mul), ('/', self.div),
                   ('clear', self.clear)]

        self.bnts = list()
        for t, c in buttons:
            self.bnts.append(tk.Button(self, text=t, command=c))

        self.result = tk.Label(self, width=30)

        #arrange
        self.num1.grid(row=0, column=0)
        self.num2.grid(row=1, column=0)
        self.result.grid(row=2, column=0)

        for i in range(len(self.bnts)):
            self.bnts[i].grid(row=i+3, column=0)

    def str_to_float(self):
        return float(self.num1.get()), float(self.num2.get())

    def add(self):
        num1, num2 = self.str_to_float()
        self.result.configure(text=f'{num1+num2}')

    def sub(self):
        num1, num2 = self.str_to_float()
        self.result.configure(text=f'{num1-num2}')

    def mul(self):
        num1, num2 = self.str_to_float()
        self.result.configure(text=f'{num1*num2}')

    def div(self):
        num1, num2 = self.str_to_float()
        self.result.configure(text=f'{num1/num2}')
        
    def clear(self):
        num1, num2 = self.str_to_float()
        self.result.configure(text='')

if __name__=='__main__':
    root = tk.Tk()

    calculator = Calculator(root)
    calculator.pack()

    root.mainloop()
