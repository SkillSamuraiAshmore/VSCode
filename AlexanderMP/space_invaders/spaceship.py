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
    invader.shape("arrow")
    invader.speed(0)
    invader.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 200)
    invader.setposition(x, y)
    invaderList.append(invader)


player = turtle.Turtle()
bullet = turtle.Turtle()

player.color("blue")
player.shape("arrow")
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(0, -250)

player_speed = 5

bullet.color("yellow")
bullet.shape("arrow")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 25
bulletstate = "ready"


def move_left():
    x = player.xcor()
    x = max(x - player_speed, -280)
    player.setx(x)

def move_right():
    x = player.xcor()
    x = min(x + player_speed, 280)
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:
    if bulletstate == "fire":
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

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

        if invader.distance(bullet) < 15:
            bullet.hideturtle()
            bulletstate = "ready"
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