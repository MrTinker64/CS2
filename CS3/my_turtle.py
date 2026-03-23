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

def square1(length):
    t.color("blue")
    t.penup()
    t.right(135)
    t.forward(length * (2 ** 0.5) / 2)
    t.left(135)
    t.pendown()
    for i in range(4):
        t.forward(length)
        t.left(90)
        
def square2(length):
    t.color("red")
    t.penup()
    t.goto(-length/2, -length/2)
    t.pendown()
    for i in range(4):
        t.forward(length)
        t.left(90)
        
square1(100)
square2(110)

turtle.update()
turtle.mainloop()