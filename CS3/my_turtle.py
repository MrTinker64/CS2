import turtle

turtle.tracer(0)
t = turtle.Turtle()

for i in range(360):
    t.forward(1)
    t.left(1)

turtle.update()
turtle.done()