from turtle import *
from random import randint
from time import sleep

clicked = False
whacked = False

max_screen_x, max_screen_y = 400, 300
border = 50
max_x, max_y = max_screen_x - border, max_screen_y - border
 
num_holes = 10
num_spins = 3

def spin():
    sleep(0.25)
    circle(10)

def print_text():
    write("Hit", align= "center", font=("Arial", 15))