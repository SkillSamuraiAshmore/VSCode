import time
import turtle
from turtle import *
from random import *

window = turtle.Screen()
window.title("Turtle Racer")
turtle.bgcolor("lightgreen")

t = turtle.Pen()
t.speed(0)
t.penup()
t.setpos(-140, 200)
t.color("white")
t.write("turtle racer!", font = ("Arial", 30, "bold"))
t.hideturtle()

t.setpos(-400, 158)
t.color ("forestgreen")
t.begin_fill()
t.pendown()

for n in range (2):
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()

stamp_size = 20
square_size = 15
finish_line = 200

t.color("black")
t.shape("square")
t.shapesize(square_size / stamp_size)
t.penup()
for i in range (10): 
    t. setpos(finish_line, (150 - (i * square_size * 2)))
    t.stamp()
for j in range (10):
    t.setpos(finish_line + square_size, (150 - square_size) - (j * square_size *2))
    t.stamp()
    
t1 = Turtle()
t1.speed(0)
t1.color("magenta")
t1.shape("turtle")
t1.penup()
t1.goto(-250, 100)

turtle.done()
    
    