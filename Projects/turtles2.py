import turtle 

t = turtle.Turtle()
t.penup()
t.goto(-100,0)
t.color("red")
t.pendown()
colors = ["yellow","red","blue"]
for i in range(200):
    t.forward(150+ i)
    t.left(100 + 1)
    t.forward(90+ i)
    t.left(60+ 1)
    t.speed(50)
    t.color( colors [i % 3])