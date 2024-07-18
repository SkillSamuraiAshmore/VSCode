import turtle
import random
turtle.bgcolor("black")

invaderList = []
number_of_invader = 5
invaderspeed = 5
for i in range (number_of_invader):
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
player.color("blue")
player.shape("arrow")
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(0, -250)

playerspeed = 15


bullet = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(0, -250)

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("arrow")
bullet.speed(0)
bullet.penup()
bullet.setheading(0.5,)
bullet.hideturtle()

bulletspeed = 25
bulletstate = "ready"
def move_left():
    x = player.xcor()
    x = max(x - playerspeed, -280)
    player.setx(x)

def move_right():
    x = player.xcor()
    x = min(x + playerspeed, 280)
    player.setx(x)

def fire_bullet():
    global bulletstate
    
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x,y)
    bullet.showturtle()
    




turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet, "space")

while True:
    if bulletstate == "fire":
        # bullet has been fired
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)
        
        






































turtle.done()