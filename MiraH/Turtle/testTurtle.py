from turtle import *

diameter = 40
pop_diameter = 300

def draw_balloon():
  a = 5
  color("purple")
  dot(diameter)
  
def inflate_balloon (): 
  global diameter
  diameter = diameter + 10
  draw_balloon()
  
  if diameter >= pop_diameter:
    clear()  
    diameter = 40
    write("POP!")
draw_balloon
inflate_balloon
onkey(inflate_balloon, "Up")
listen()





done()
