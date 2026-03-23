import turtle

turtle.tracer(0)
t = turtle.Turtle()

s = turtle.Screen()
s.setup(1000,1000)
s.title('CS 3')
s.bgcolor('skyblue')

# for i in range(360):
#     t.forward(1)
#     t.left(1)

# def doSomething(x,y):
#    t.goto(x,y)
#    t.shape('circle')
#    t.shapesize(2.5,2.5,2.5)
#    t.stamp()

# s.onscreenclick(doSomething)

turtle.update()
turtle.mainloop()