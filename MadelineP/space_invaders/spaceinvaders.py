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
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed =  25
bullet_state = "ready"


def move_left():
    x = player.xcor()
    x = max(x - playerspeed, -280)
    player.setx(x)

def move_right():
    x = player.xcor()
    x = min(x + playerspeed, 280)
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

turtle.done()
