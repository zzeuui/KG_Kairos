import turtle as t

def goto_pen(x, y, c, r):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.pensize(3)
    t.color(c)
    t.circle(r)

goto_pen(0, 0, "black", 50)

goto_pen(100, 0, "red", 50)

goto_pen(-100, 0, "blue", 50)

goto_pen(-50, -50, "yellow", 50)

goto_pen(50, -50, "green", 50)
