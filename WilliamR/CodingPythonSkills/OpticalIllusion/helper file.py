import math
"""
drawline:draws a line from one point to another
"""
def drawline(turtle, x1, y1, x2,y2,colour="black"):
    turtle.penup()
    turtle.goto(x2, y1)
    turtle.pendown()  
    turtle.color(colour)
    turtle.goto(x2, y2)
    
    
    """
    drawcircle draws circle
    """
    
    
def drawCircle(turtle, x, y, radius, colour="black" ,angle=0, fill=True):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)
    if fill: turtle.begin_fill()
    