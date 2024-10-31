import turtle
from helperfile import drawTriangle

turtle.speed(0)
turtle.hideturtle
turtle.Screen().tracer(0,0)
 
def sierpinsky(x, y, size, degree):
    drawTriangle(turtle, x, y, size, fill=False)
    colours = ['blue','red','green', 'white','yellow','violet', 'orange']
    
    drawTriangle(turtle, x, y, size, colours[degree])

    if degree > 0:
        sierpinsky( x, y, size/2,  degree-1)
        sierpinsky(x + size/2, y, size/2, degree-1) 
        sierpinsky(x + size/4, y + size*0.43, size/2, degree-1)
  
sierpinsky(-350, -350, 700, 6)


turtle.done()