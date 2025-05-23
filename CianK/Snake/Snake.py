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
snakeFood.shape("circle")
snakeFood.shapesize(0.5, 0.5)
snakeFood.speed(0)
snakeFood.penup()
snakeFood.goto(0,100)


def move():
    position = snakeHead.position()
    

    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor() + 20)
    elif snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor() - 20)
    elif snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor() + 20)
    elif snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor() - 20)

    for segment in segments:
        newPosition = segment.position()
        segment.goto(position)
        position = newPosition

    
        kill_snake()
    for segment in segments:
        if segment.distance(snakeHead) < 10:
            kill_snake()



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

def kill_snake():
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
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        snakeFood.goto(x, y)
        snakeSegment = snakeHead.clone()
        snakeSegment.color("black")
        segments.append(snakeSegment)
        score = score + 10
        update_score()

