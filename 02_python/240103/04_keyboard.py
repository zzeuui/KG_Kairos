from turtle import *

class Keyboard():
    def __init__(self, screen, t):
        self.screen = screen
        self.t = t

        self.pen_size = 1
        self.pen_mode = 1

        self.screen.title(f"Turtle - pen size:{self.pen_size} pen: {self.pen_mode}")

    def forward_move(self):
        self.t.pensize(self.pen_size)
        self.t.forward(10)

    def backward_move(self):
        self.t.pensize(self.pen_size)
        self.t.backward(10)

    def turn_left(self):
        self.t.pensize(self.pen_size)
        self.t.left(10)

    def turn_right(self):
        self.t.pensize(self.pen_size)
        self.t.right(10)

    def clear_all(self):
        self.t.home()
        self.t.clear()

    def increase_pen(self):
        self.pen_size += 1
        self.screen.title(f"Turtle - pen size:{self.pen_size} pen: {self.pen_mode}")

    def decrease_pen(self):
        self.pen_size -= 1
        if self.pen_size < 1:
            self.pen_size = 1

        self.screen.title(f"Turtle - pen size:{self.pen_size} pen: {self.pen_mode}")

    def pen_onoff(self):
        self.pen_mode = not self.pen_mode
        if self.pen_mode:
            self.t.pendown()
        else:
            self.t.penup()
        self.screen.title(f"Turtle - pen size:{self.pen_size} pen: {self.pen_mode}")

def set_screen(screen, t, k):

    key_func = {'Up': k.forward_move,
                'Down': k.backward_move,
                'Left': k.turn_left,
                'Right': k.turn_right,
                'c': k.clear_all,
                'w': k.increase_pen,
                'e': k.decrease_pen,
                'q': k.pen_onoff,
                'a': t.undo}
    
    for k, func in key_func.items():
        screen.onkeypress(func, k)

    screen.listen()

if __name__=='__main__':
    screen = Screen()
    screen.title("Turtle")

    t = Turtle()
    k = Keyboard(screen, t)

    set_screen(screen, t, k)

    done()
