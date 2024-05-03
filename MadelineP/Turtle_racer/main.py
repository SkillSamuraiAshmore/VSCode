import time
import turtle
from turtle import *
from random import *

window = turtle.Screen()
window.title("Turtle Racer")
turtle.bgcolor("lightgreen")

t = turtle.pen()
t.speed(0)
t.penup()
t.setpos(-140, 200)
t.color("white")
t.write("Turtle Racer!", font = ("Arial", 30, "bold"))
t.hideturtle()

t.setpos(-400, 158)
t.color("forestgreen")
t.begin_fill()
t.pendown()

for n in range (2):
    t.foward(800)
    t.right(90)
    t.foward(300)
    t.right(90)
t.end_fill()

stamp_size = 20
square_size = 15
finish_line = 200

t.color("black")
t.shape("square")
t.shapesize(square_size / stamp_size)
