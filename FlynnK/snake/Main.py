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
snakeHead.speed(100)
snakeHead.direction = "stop"
delay = 0
segments = []
score = 0

scoreLable = turtle.Turtle()
scoreLable.penup()
scoreLable.hideturtle()
scoreLable.goto(-280, 260)
scoreLable.write("Score: " + str(score), font = ("Arial", 24, "normal"))

def update_score():
    scoreLable.clear()
    scoreLable.write("Score: " + str(score), font = ("Arial", 24, "normal"))

snakeFood = turtle.Turtle()
snakeFood.color("red")
snakeFood.shape("square")
snakeFood.shapesize(1, 1)
snakeFood.speed(0)
snakeFood.penup()
snakeFood.goto(0,100)

#BetterFood = turtle.Turtle()
#BetterFood.shape("square")
#BetterFood.shapesize(0.5, 0.5)
#BetterFood.speed(0)
#BetterFood.penup()
#BetterFood.goto(0,100)

def move():
    position = snakeHead.position()
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor() + 20)
    if snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor() - 20)
    if snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor() + 20)
    if snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor() - 20)
        
    for segment in segments:
        newPosition = segment.position()
        segment.goto(position)
        position = newPosition
        
    if snakeHead.xcor() >= 290 or snakeHead.xcor() <= -290 or snakeHead.ycor() >= 290 or snakeHead.ycor() <= -290:
        Kill_snake()
    for segment in segments:
        if segment.distance(snakeHead) < 10:
            Kill_snake()
        
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
        
def Kill_snake():
    global segments, delay, score
    for segment in segments:
        segment.color("red")
        time.sleep(delay)
        snakeScreen.update()
    time.sleep(1)
    for segment in reversed(segments):
        segment.hideturtle()
        time.sleep(delay)
        snakeScreen.update()
    segments = []
    snakeHead.goto(0,0)
    snakeHead.direction = "stop"
    delay = 0.1
    score = 0
    update_score()
        

snakeScreen.onkeypress(move_up , 'w')
snakeScreen.onkeypress(move_down , 's')
snakeScreen.onkeypress(move_left , 'a')
snakeScreen.onkeypress(move_right , 'd')
snakeScreen.listen()

while True:
    snakeScreen.update()
    move()
    time.sleep(delay)
    if snakeHead.distance(snakeFood) < 15:
        X = random.randint(-270, 270)
        Y = random.randint(-270, 270)
        snakeFood.goto(X, Y)
        snakeSegments = snakeHead.clone()
        snakeSegments.color("grey")
        segments.append(snakeSegments)
        score = score + 1
        update_score()