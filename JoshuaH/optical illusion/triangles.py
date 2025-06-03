import turtle;
from illusion_helper import drawTriangle;

turtle.speed(0);
turtle.hideturtle();
turtle.Screen().tracer(0,0);


def sierpinski(x, y, size, degree):
    colours = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange'];
    
    drawTriangle(turtle, x, y, size, colours[degree]);
    
    if degree >0:
        sierpinski(x, y, size/2, degree-1);
        sierpinski(x + size/2, y, size/2, degree-1);
        sierpinski(x + size/4, y + size*0.43, size/2,degree-1);
    
sierpinski(-350, -350, 700, 6);

turtle.done();