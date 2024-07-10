import turtle
import random

turtle.bgcolor("black")

invaderList = []
number_of_invaders = 5
invaderspeed = 5

score = 0

for i in range(number_of_invaders):
    invader = turtle.Turtle()
    invader.color("red")
    invader.shape("square")
    invader.speed(0)
    invader.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 200)
    invader.setposition(x, y)
    invaderList.append(invader)

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

bullet_speed =  20
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

while True:
    if bullet_state == "fire":
        y = bullet.ycor() 
        y = y + bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    for invader in invaderList:
        x = invader.xcor()
        x = x + invaderspeed
        invader.setx(x)

        if invader.xcor() > 280 or invader.xcor() < -280:
            invaderspeed = invaderspeed * -1

            for invader in invaderList:
                y = invader.ycor()
                y = y - 25
                invader.sety(y)
                print("ran y down")
        
        if invader.distance(bullet) < 15:
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)

            x = random.randint(-200, 200)
            y = random.randint(100, 200)
            invader.setposition(x, y)

            score += 10

        if invader.distance(player) < 15:
            player.hideturtle()
            invader.hideturtle()
            print("your score was: ", score)
    
    
turtle.done()
