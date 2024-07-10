import turtle
from IllusionHelper import drawSquare, drawDiamond

turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)

def drawPrimerose(x, y, size, colour):
    drawDiamond(turtle, x, y, size, colour, angle=0)
    drawDiamond(turtle, x, y, size, colour, angle=90)
    drawDiamond(turtle, x, y, size, colour, angle=180)
    drawDiamond(turtle, x, y, size, colour, angle=270)

gridSize = 45
gridColour1 = "#59b983"
gridColour2 = "#a4d443"

drawSquare(turtle, -7*gridSize, -7*gridSize, 15*gridSize, gridColour1)


for x in range(-7, 8, 2):
    for y in range(-7, 8, 2):
        drawSquare(turtle, gridSize*x, gridSize*y, gridSize, gridColour2)

for x in range(-6, 8, 2):
    for y in range(-6, 8, 2):
        drawSquare(turtle, gridSize*x, gridSize*y, gridSize, gridColour2)

primroseSize = 6
primroseColour1 = "white"
primroseColour2 = "#c81d97"
pattern = [primroseColour1, primroseColour2, primroseColour2, primroseColour1,
          primroseColour2, primroseColour1, primroseColour1, primroseColour2]

for y in range(-6, 8, 1):
    for x in range(-6, 8, 1):
        drawPrimerose(gridSize*x, gridSize*y, primroseSize, pattern[(x+y-1)%8])


temp = input("")
