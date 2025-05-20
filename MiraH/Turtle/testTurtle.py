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
  
draw_balloon
inflate_balloon()
done()