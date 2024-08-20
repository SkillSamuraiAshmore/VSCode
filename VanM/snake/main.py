import turtle
import random
import time

snakeScreen = turtle.Screen()
snakeScreen.title ("EATFOODFOREVERSIM")
snakeScreen.setup(width = 600, height = 600)
snakeScreen.tracer(0)

snakeHead = turtle.Turtle()
snakeHead.shape("square")
snakeHead.penup()
snakeHead.speed(0)
snakeHead.direction = "stop"

delay = 0.2
snakeSegments = []
score = 0

scoreLabel=turtle.Turtle()
scoreLabel.penup()
scoreLabel.hideturtle()
scoreLabel.goto(-280, 260)
scoreLabel.write("Score: " + str(score), font = ("Arial", 24, "normal"))

def update_score():
    scoreLabel.clear()
    scoreLabel.write("Score: " + str(score), font = ("Arial", 24, "normal"))



food = turtle.Turtle()
food.color("yellow")
food.shape("circle")
food.shapesize(0.5, 0.5)
food.speed(0)
food.penup()
food.goto(0,100)

def move():
    
    position = snakeHead.position()
    
    if snakeHead.direction == "up":
        snakeHead.sety(snakeHead.ycor() + 20)
    if snakeHead.direction == "down":
        snakeHead.sety(snakeHead.ycor() - 20)
    if snakeHead.direction == "right":
        snakeHead.setx(snakeHead.xcor() + 20)
    if snakeHead.direction == "left":
        snakeHead.setx(snakeHead.xcor() + - 20)
        
        
    for segment in snakeSegments:
        newPosition = segment.position()
        segment.goto(position)
        position = newPosition
        
    if snakeHead.xcor() >= 290 or snakeHead.xcor() <= -290 or snakeHead.ycor() >= 290 or snakeHead.ycor() <= -290:
        operation_Kill_snake()
    for segment in snakeSegments:
        if segment.distance(snakeHead) < 10:
            operation_Kill_snake()
            
            
            
                          
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
        
        
def operation_Kill_snake():
            global segments, delay, score
            for segment in segments:
                segment.color("yellow")
                time.sleep(delay)
                snakeScreen.update()
            time.sleep(1)
            for segment in reversed(segments):
                segment.hideturtle
                time.sleep(delay)
                snakeScreen.update()
                
            segments = []
            snakeHead.goto(0,0)
            snakeHead.direction
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
    if snakeHead.distance(food) < 15:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x , y)
        snakeSegment = snakeHead.clone()
        snakeSegment.color("green")
        snakeSegments.append(snakeSegment)
        score = score + 10
        update_score()