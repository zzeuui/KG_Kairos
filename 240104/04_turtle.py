import turtle as t

n = int(input())
if 3 <= n <= 9:
    angle = 180-((180*(n-2))/n)
    for _ in range(n):
        t.right(angle)
        t.forward(100)
t.done()
