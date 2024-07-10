import turtle
import random
import time

snake_screen = turtle.Screen()
snake_screen.title("Snake")
snake_screen.setup(width=600, height=600)
snake_screen.tracer(0)

snakeHead = turtle.Turtle()
snakeHead.shape("square")
snakeHead.penup()
snakeHead.speed(0)
snakeHead.direction = "stop"

delay = 0.2
segments = []
score = 0

scoreLabel = turtle.Turtle()
scoreLabel.penup()
scoreLabel.hideturtle()
scoreLabel.goto(-280, 260)
scoreLabel.write("Score: " + str(score), font=("Arial", 24, "normal"))

def update_score():
    scoreLabel.clear()
    scoreLabel.write("Score: " + str(score), font=("Arial", 24, "normal"))

snakeFood = turtle.Turtle()
snakeFood.color("red")
snakeFood.shape("circle")
snakeFood.shapesize(0.5, 0.5)
snakeFood.speed(0)
snakeFood.penup()
snakeFood.goto(0, 100)

def move():
    position = snakeHead.pos()
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
    
    if snakeHead.xcor() >= 290 or snakeHead.xcor() >= -290 or snakeHead.ycor() >= 290 or snakeHead.ycor() >= -290:
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
        snake_screen.update()
    time.sleep(1)
    for segment in reversed(segments):
        segment.hideturtle()
        time.sleep(delay)
        snake_screen.update()
    segments = []
    snakeHead.goto(0, 0)
    snakeHead.direction = "stop"
    delay = 0.1
    score = 0
    update_score()

snake_screen.onkeypress(move_up, 'w')
snake_screen.onkeypress(move_down, 's')
snake_screen.onkeypress(move_left, 'a')
snake_screen.onkeypress(move_right, 'd')
snake_screen.listen()

while True:
    snake_screen.update()
    move()
    time.sleep(delay)
    if snakeHead.distance(snakeFood) < 15:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        snakeFood.goto(x, y)
        snakeSegment = snakeHead.clone()
        snakeSegment.color("grey")
        segments.append(snakeSegment)
        score = score + 10
        update_score()
        
