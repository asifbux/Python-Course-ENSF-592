import turtle
import math

bob = turtle.Turtle()

size = 100 # size of the polygon
n = 40 # number of sides
angle = 360/n
for i in range(60):
       size = (size*(math.sqrt(3)/2)) / math.sin(math.radians(70))
       bob.forward(size)
       bob.left(60)
