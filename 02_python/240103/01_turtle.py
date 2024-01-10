import turtle as t

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

my_t = t.Turtle()

my_t.penup()
my_t.goto(0, 250)
my_t.pendown()
my_t.write("hello world", font=('Arial', 15,))
my_t.ht()
