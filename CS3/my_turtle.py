import turtle

t = turtle.Turtle()

s = turtle.Screen()
s.setup(1000,1000)
s.title('CS 3')
s.bgcolor('skyblue')

turtle.tracer(0)



# def outline():
#     s.bgcolor('red')
#     t.shape("turtle")
#     t.shapesize(2)
#     t.hideturtle()
#     t.color('blue')
#     t.stamp()
#     t.shapesize(1.5)
#     t.color('red')
#     t.stamp()
    
# outline()

# def squareOnClick(x, y):
#     turtle.tracer(0)
#     length = 100
#     t.penup()
#     t.goto(x-length/2, y-length/2)
#     t.pendown()
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
#     turtle.update()

# s.onscreenclick(squareOnClick)

# for i in range(360):
#     t.forward(1)
#     t.left(1)

# def doSomething(x,y):
#    t.goto(x,y)
#    t.shape('circle')
#    t.shapesize(2.5,2.5,2.5)
#    t.stamp()

# s.onscreenclick(doSomething)

# def square1(length):
#     t.color("blue")
#     t.penup()
#     t.right(135)
#     t.forward(length * (2 ** 0.5) / 2)
#     t.left(135)
#     t.pendown()
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
        
# def square2(length):
#     t.color("red")
#     t.penup()
#     t.goto(-length/2, -length/2)
#     t.pendown()
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
        
# square1(100)
# square2(110)

turtle.update()
turtle.mainloop()