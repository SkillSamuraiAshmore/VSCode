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

scoreLabel = turtle.Turtle()
scoreLabel.penup()
scoreLabel.hideturtle()
scoreLabel.goto(-280, 260)
scoreLabel.write("Score " + str(score), font = ("Arial", 24, "normal"))

def update_score():
    scoreLabel.clear()
    scoreLabel.write("Score " + str(score), font = ("Arial", 24, "normal"))

snakeFood = turtle.Turtle()
snakeFood.color("blue")
snakeFood.shape("circle")
snakeFood.shapesize(0.5, 0.5)
snakeFood.speed(0)
snakeFood.penup()
snakeFood.goto(0,100)


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
    
    for segement in segments:
        newPosition = segement.position()
        segement.goto(position)
        position = newPosition
    
    if snakeHead.xcor() >= 290 or snakeHead.xcor() <= -290 or snakeHead.ycor() >= 290 or snakeHead.ycor() <= -290:
        kill_snake()
    for segement in segments:
        if segement.distance(snakeHead) < 10:
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
    for segement in segments:
        segement.color("red")
        time.sleep(delay)
        snakeScreen.update()
    time.sleep(1)
    for segement in reversed(segments):
        segement.hideturtle()
        time.sleep(delay)
        snakeScreen.update()
    segments = []
    snakeHead.goto(0, 0)
    snakeHead.direcion = "stop"
    delay = 0.1
    score = 0
    update_score()
    
    
    

            
snakeScreen.onkeypress(move_up , 'w')
snakeScreen.onkeypress(move_down , 's')
snakeScreen.onkeypress(move_right , 'd')
snakeScreen.onkeypress(move_left , 'a')
snakeScreen.listen()

while True: 
    snakeScreen.update()
    move()
    time.sleep(delay)
    if snakeHead.distance(snakeFood) < 15:
        X = random.randint(-270, 270)
        Y = random.randint(-270, 270)
        snakeFood.goto(X,Y)
        snakeSegment = snakeHead.clone()
        snakeSegment.color("brown")
        segments.append(snakeSegment)
        score = score + 1
        update_score()
        
    




turtle.done()