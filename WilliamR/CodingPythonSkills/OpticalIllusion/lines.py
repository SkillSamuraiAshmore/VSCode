import turtle
from  helperfile import drawLine, drawCircle
turtle.speed(0)
turtle.pensize(2)

drawLine(turtle, -250, 100, -50, 100, "purple")

drawCircle(turtle, -250, 100, 20, "purple", angle=270, fill=False)
drawCircle(turtle, -50, 100, 20, "purple", angle=90, fill=False)


drawLine(turtle, 50, 100, 250, 100, "purple")
drawCircle(turtle, 50, 100, 20, "purple", angle=90, fill=False)
drawCircle(turtle, 250, 100, 20, "purple", angle=270, fill=False)

drawLine(turtle, 50, -100, 250, -100, "purple")
drawLine(turtle, 50, -100, 80, -70, "purple")
drawLine(turtle, 50, -100, 80, -70, "purple")
drawLine(turtle, 50, -100, 80, -30, "purple")
drawLine(turtle, 250, -100, 220, -70, "purple")



















turtle.done()