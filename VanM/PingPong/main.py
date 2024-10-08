import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)



#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")

# TODO: paddle b

#ball 


#Main_Game_Loop
while True:
    win.update()
    