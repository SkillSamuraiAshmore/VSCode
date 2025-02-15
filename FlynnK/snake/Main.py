import turtle
import random
import time

snakeScreen = turtle.Screen()
snakeScreen.title("Snake")
snakeScreen.setup(width = 600, height = 600)
snakeScreen.tracer

snakeHead = turtle.Turtle()
snakeHead. shape("square")
snakeHead.penup()
snakeHead.speed(0)
snakeHead.direction = "stop"

def move():
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor() + 20)
    if snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor() - 20)
    if snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor() + 20)
    if snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor() - 20)