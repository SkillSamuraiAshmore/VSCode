# Junior Engineers Optical Illusion helper functions

import math

"""
drawLine: draws a line from one point to another
"""
def drawLine(turtle, x1, y1, x2, y2, colour="black"):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(colour)
    turtle.goto(x2, y2)

"""
drawCircle: draws a circle
"""
def drawCircle(turtle, x, y, radius, colour="black", angle=0, fill=True):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)
    if fill: turtle.begin_fill()
    turtle.circle(radius)
    if fill: turtle.end_fill()
    

"""
drawSquare: draws a square
"""
def drawSquare(turtle, x, y, size, colour="black", angle=0, fill=True):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)    
    if fill: turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    if fill: turtle.end_fill()
    
"""
drawSquare: draws a square
"""
def drawRectangle(turtle, x, y, width, height, colour="black", angle=0, fill=True):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)    
    if fill: turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    if fill: turtle.end_fill()

"""
drawTriangle: draws a triangle
"""
def drawTriangle(turtle, x, y, size, colour="black", angle=0, fill=True):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)    
    if fill: turtle.begin_fill()
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    if fill: turtle.end_fill()

"""
drawDiamond: draws a diamond
"""
def drawDiamond(turtle, x, y, size, colour="black", angle=0, fill=True):
    turtle.setheading(angle + 60)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)    
    if fill: turtle.begin_fill()
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    if fill: turtle.end_fill()
    
"""
drawElipse: draws an oval
"""
def drawEllipse(turtle, cx, cy, width, height, colour="black", angle=0, fill=True):
    t = -math.pi/2
    a = angle*math.pi/180
    x = cx + width*math.cos(t)*math.cos(a) - height*math.sin(a)*math.sin(t)
    y = cy + height*math.sin(t)*math.cos(a) + width*math.sin(a)*math.cos(t)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)
    if fill: turtle.begin_fill()
    for _ in range(100):
        x = cx + width*math.cos(t)*math.cos(a) - height*math.sin(a)*math.sin(t)
        y = cy + height*math.sin(t)*math.cos(a) + width*math.sin(a)*math.cos(t)
        turtle.goto(x,y)    
        t += 2*math.pi/100
    if fill: turtle.end_fill()
  