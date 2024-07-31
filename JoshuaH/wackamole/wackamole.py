from turtle import *
from random import randint 
from time import sleep 

clicked = False
whacked = False

max_screen_x, max_screen_y = 400, 300
border = 50
max_x = max_screen_x-border
max_y = max_screen_y-border

num_holes = 10
num_spins = 3

def spin():
    sleep(0.25)
    circle(10)
    
def print_text():
    write("Hit!", align="center", font=("Arial", 15, "bold"))
    
def dig():
    dot(50)

def near_mole(x_coord, y_coord):
    leeway = 20
    return (x_coord - leeway <=xcor() <= x_coord + leeway) and \
            (y_coord - leeway <= ycor() <= y_coord + leeway )
            
def move_mole():
    global clicked, whacked
    new_x, new_y = randint(-max_x, max_x), randint(-max_y, max_y)
    goto(new_x, new_y)
    
    spin_count = 0
    while not clicked and spin_count < num_spins:
        spin()
        spin_count += 1
        
    if whacked:
        print_text()
    else:
        dig()
    
    clicked = False
    whacked = False
    
def whack(x_coord, y_coord)
     global clicked, whacked
     clicked = True
     whacked = near_mole(x_coord, y_coord)
     
     