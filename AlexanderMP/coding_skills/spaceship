import turtle
import random
turtle.bgcolor("black")
player = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(0, -250)

playerspeed = 15


bullet = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(0, -250)


def move_left():
    x = player.xcor()
    x = max(x - playerspeed, -280)
    player.setx(x)

def move_right():
    x = player.xcor()
    x = min(x + playerspeed, 280)
    player.setx(x)

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right,"Right")









































turtle.done()