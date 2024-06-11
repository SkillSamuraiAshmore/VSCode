import time
import turtle
from turtle import *
from random import *

window = turtle.Screen()
window.title("Turtle Racer 1.0")
turtle.bgcolor("lightgreen")

t = turtle.Pen()
t.speed(0)
t.penup()
t.setpos(-140, 200)
t.color("white")
t.write("Turtle Racer", font = ("Arial", 30, "bold"))
t.hideturtle()

t.setpos(-400, 158)
t.color("forestgreen")
t.begin_fill()
t.pendown()

for n in range (2):
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()


turtle.done()





