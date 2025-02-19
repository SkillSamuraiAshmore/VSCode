from turtle import *
from random import randint
from time import sleep 

clicked = False
whacked = False

max_screen_x, max_screen_y = 500, 300
border = 100
max_x, max_y = max_screen_x - border, max_screen_y - border

num_holes = 10
num_spins = 3

def spin():
    sleep(0.25)
    circle(10)
def print_text():
     write("Hit!!!", aligh="centre", font=(arial, 15, "normal"))

def dig():
    dot(50)
    
def near_mole(x_coord, y_coord):
    leeway = 20
    return (x_coord - leeway <= xcor() <=x_coord + leeway) and \ (y_coord - leeway )
        
    
