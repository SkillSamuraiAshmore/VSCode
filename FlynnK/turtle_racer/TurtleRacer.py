import time
import turtle
from turtle import *
from random import *

window = turtle.Screen()
window.title("Turtle racer")
turtle.bgcolor("lightblue")

t = turtle.Pen()
t.speed(0)
t.penup()
t.setpos(-140, 200)
t.color("red")
t.write("Turtle Racer!", font = ("Arial", 30, "bold"))
t.hideturtle()

t.setpos(-400, 158)
t.color("white")
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
    t.setpos(finish_line, (150 - (i * square_size * 2)))
    t.stamp()
for j in range (10):
    t.setpos(finish_line + square_size, (150 - square_size) - (j * square_size * 2))
    t.stamp()

t1 = Turtle()
t1.speed(0)
t1.color("green")
t1.shape("turtle")
t1.penup()
t1.goto(-250, 100)

t2 = Turtle()
t2.speed(0)
t2.color("pink")
t2.shape("turtle")
t2.penup()
t2.goto(-250, 50)

t3 = Turtle()
t3.speed(0)
t3.color("blue")
t3.shape("turtle")
t3.penup()
t3.goto(-250, 0)

t4 = Turtle()
t4.speed(0)
t4.color("red")
t4.shape("turtle")
t4.penup()
t4.goto(-250, -50)

t5 = Turtle()
t5.speed(0)
t5.color("gray")
t5.shape("turtle")
t5.penup()
t5.goto(-250, -100)

time.sleep(2)

for i in range (140):
    t1.forward(randint(1,5))
    t2.forward(randint(1,6))
    t3.forward(randint(2,6))
    t4.forward(randint(1,6))
    t5.forward(randint(-1,8))




while True:
    print("")