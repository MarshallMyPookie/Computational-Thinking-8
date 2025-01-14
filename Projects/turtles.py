import turtle 

t = turtle.Turtle()
t.penup()
t.goto(-100,0)
t.color("red")
t.pendown()
colors = ["yellow","red","blue"]
for i in range(1000):
    t.forward(150+ i)
    t.left(120 + 1)
    t.speed(50)
    t.color( colors [i % 3])




turtle.exitonclick()