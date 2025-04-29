from turtle import *
from random import *
def star(height, colour):
    
    left_angle = 72
    right_angle = 144
    line_size = height * 0.409
    
    setheading(-left_angle)
    color(colour)
    pendown()
    begin_fill()
    segment_numbers = range(5)
    for seg_no in segment_numbers:
        forward(line_size)
        left(left_angle)
        forward(line_size)
        right(right_angle)
    end_fill()
    penup()

star_count = input("Please enter how many stars you want to see: ")
star_count = int(star_count)

speed("fastest")

setup(800, 800)
bgcolor("dark blue")
penup()

for star_num in range(star_count):
    x_pos = randint(-400, 400)
    y_pos = randint(-400, 400)
    
    size = randint(5, 20)
    colour = choice(['white', 'black', 'light blue', 'blue'])
    
    goto(x_pos, y_pos)
    
    star(size,colour)
    
temp = input("")
