import turtle

# Turtle and Screen Initialization
t = turtle.Turtle()
s = turtle.Screen()
s.setup(600, 600)

t.penup()
t.hideturtle()
s.tracer(0)
    
count = 0

def playMove(x,y):
    global count
    count += 1
    # t.clear()
    t.goto(x, y)
    t.write(count)
    # s.update()

turtle.onscreenclick(playMove)
turtle.mainloop()
