import turtle 
####setup
t = turtle.Turtle()
t.penup()
t.goto(-100,0)
t.color("red")
t.pendown()
##this is the part where we decide colors
colors = ["yellow","red","blue"]
for i in range(1000):
    t.forward(150+ i)
    t.left(120 + 1)
    t.speed(150)
    t.color( colors [i % 3])



###this part means it disappears when you click the screen
turtle.exitonclick()