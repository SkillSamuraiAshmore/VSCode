import turtle

wn = turtle.Screen()
wn.title("pong by will")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1 )
paddle_a.penup()
paddle_a.goto(-350, 0)
#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1 )
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.4


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_a.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_b.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")
#main game loop
while True:
    wn.update()
    
#move ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
#border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
   
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
   
   
   
   
   