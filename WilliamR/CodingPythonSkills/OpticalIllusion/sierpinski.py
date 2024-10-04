import turtle
from helperfile import drawTriangle

turtle.speed(0)


def sierpinsky(x, y, size, degree):
    drawTriangle(turtle, x, y, size, fill=False)
    drawTriangle(turtle, x, + size/2, fill=False)
    drawTriangle(turtle, x, + size/4, y + size*0.43, size/2, fill=False)
  
sierpinsky(-350, -350, 700, 1)

turtle.done()