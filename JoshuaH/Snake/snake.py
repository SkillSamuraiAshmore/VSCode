import turtle
import random
import time

snakeScreen = turtle.Screen()
snakeScreen.title("Snake")
snakeScreen.setup(width = 600, height = 600)
snakeScreen.tracer(0)

snakeHead = turtle.Turtle() 
snakeHead.shape("square")
snakeHead.penup()
snakeHead.speed(0)
snakeHead.direction = "stop"

delay = 0.2

snakeFood = turtle.Turtle()
snakeFood.color("green")
snakeFood.shape("triangle")
snakeFood.shapesize(0.5, 0.5)
snakeFood.speed(0)
snakeFood.penup()
snakeFood.goto(0,100)

def move():
    if snakeHead.direction =="up":
        snakeHead.sety(snakeHead.ycor() + 20)
    if snakeHead.direction =="down":
        snakeHead.sety(snakeHead.ycor() - 20)
    if snakeHead.direction =="right":
        snakeHead.setx(snakeHead.xcor() + 20)
    if snakeHead.direction =="left":
        snakeHead.setx(snakeHead.xcor() - 20)
        
def move_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
def move_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
def move_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
def move_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
        
snakeScreen.onkeypress(move_up, 'w')
snakeScreen.onkeypress(move_down, 's')
snakeScreen.onkeypress(move_left, 'a')
snakeScreen.onkeypress(move_right, 'd')
snakeScreen.listen()

while True:
    snakeScreen.update()
    move()
    time.sleep(delay)
    if snakeHead.distance(snakeFood) < 15:
        pass
    
turtle.done()