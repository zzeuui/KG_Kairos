import turtle as t

t.setpos(0, 0)

t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.color("orange")
t.circle(100)

t.penup()
t.setpos(-20, 100)
t.pendown()
t.left(90)
t.circle(30, 180)

t.penup()
t.setpos(100-20, 100)
t.pendown()
t.left(180)
t.circle(30, 180)

t.begin_fill()
t.penup()
t.setpos(-40, 70)
t.pendown()
t.circle(40, 180)

t.left(90)
t.forward(80)
t.end_fill()

t.ht()
t.done()

