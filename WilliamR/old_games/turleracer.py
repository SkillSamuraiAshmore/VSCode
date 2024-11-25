import time
import turtle
from turtle import *
from random import *

window = turtle.Screen()
window.title("turtle racer")
turtle.bgcolor("lightgreen")

t = turtle.Pen()
t.speed(0)
t.penup()
t.setpos(- 140,200)
t.color("white")
t.write("turtle racer", font = ("ariel", 30,"bold"))
t.hideturtle()
t.setpos(-400, 158)
t.colour("blue")
t.begin_fill
t.pendowm()
temp = input("")
for n in range(2):
    t.forward(800)
    t.right
