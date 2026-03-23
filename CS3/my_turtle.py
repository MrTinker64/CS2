import turtle

t = turtle.Turtle()

s = turtle.Screen()
s.setup(1000,1000)
s.title('CS 3')
s.bgcolor('skyblue')

turtle.tracer(0, 0)

def tree(level, size, sizeFactor, leftAngle, rightAngle):
    t.forward(size)
    if level > 0:
        t.left(leftAngle)
        tree(level-1, size*sizeFactor, sizeFactor, leftAngle, rightAngle)
        t.right(leftAngle + rightAngle)
        tree(level-1, size*sizeFactor, sizeFactor, leftAngle, rightAngle)
        t.left(rightAngle)
    t.back(size)

t.setheading(90)
tree(4, 200, 0.75, 90, 90)

# 5a: tree(4, 45, 0.9, 30, -10)
# 5c: tree(4, 10, 1.7, 15, 15)
# 5d: tree(10, 45, 0.9, 22.5, 22.5)
# 5e: tree(4, 200, 0.75, 90, 90)

# def tree(level, size):
#     t.forward(size)
#     if level > 0:
#         t.left(45)
#         tree(level-1, size/2)
#         t.right(90)
#         tree(level-1, size/2)
#         t.left(45)
#     t.back(size)

# t.setheading(90)        
# tree(10, 100)

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