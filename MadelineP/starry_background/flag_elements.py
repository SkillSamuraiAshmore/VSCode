from turtle import *


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