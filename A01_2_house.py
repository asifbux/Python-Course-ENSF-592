"""This is the summary line

In this program. We will ask user for the size of the house they
want using turtle module in python.
"""

import turtle
import math

# Ask User & setup the variables
lengthHouse = int(input("Whats the size of your house in pixel? "))
diagonalHouse = math.sqrt(lengthHouse**2 + lengthHouse**2)  # using pythagoream threaom
slantHeight = diagonalHouse / 2

# Draw the Turtle
turtle.left(45)
turtle.forward(diagonalHouse)
turtle.left(135)
turtle.forward(lengthHouse)
turtle.right(135)
turtle.forward(slantHeight)
turtle.right(90)
turtle.forward(slantHeight)
turtle.right(45)
turtle.forward(lengthHouse)
turtle.right(135)
turtle.forward(diagonalHouse)
turtle.left(135)
turtle.forward(lengthHouse)
turtle.left(90)
turtle.forward(lengthHouse)


# End the program

turtle.done()
