from turtle import *
from random import *
from flag_elements import *

star_count = input("How many stars do you want to see?: ")

star_count = int(star_count)

speed("fastest")

setup(800, 800)
bgcolor("dark blue")
penup()

for star_num in range (star_count):
   x_pos = randint(-400, 400)
   y_pos = randint(-400, 400)

   size = randint(5, 20)
   colour = choice(['yellow', 'honeydew', 'gold', 'goldenrod', 'wheat',
                   'white', 'white smoke'])
   
   goto(x_pos, y_pos)

   star(size, colour)