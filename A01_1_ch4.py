import turtle
import math
'''turtle with lowercase t provides a
fuction called Turtle with an uppercase T
bob refers to an object with type Turtle in module turtle'''

bob = turtle.Turtle()

# for i in range(4):
#     bob.forward(100)
#     bob.left(90)

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(bob, 200)

def polygon(t, length, n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)

polygon(bob, 8, 20)

def circle(t, r):
    n = 30
    length = (2 * math.pi * r)/n
    polygon(t, length, n)
circle(bob, 20)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1 #fraction of arc to draw
    for i in range(n):
        t.forward(arc_length/n)
        t.left(angle/n)

arc(bob, 50, 160)

turtle.done() # same as turtle.mainloop()


'''
Things that I learnd:
1) import different python libraries such as math and turtle
2) how to design algorithm on paper and then put in code.
3) first I had my variables declared inside the def but the prof
told me to declare it outside the def fuctions which made my codes
much easier to read.
4) Creating multiple functions and using different parameters
5) It was the first interaction with GUI package in python
6) I also used many other turtle fuctions such as .fullcolor() and
.color() when practicing
6) For arc, I had to ask for help from the professor as I did not understand clearly
from the textbook
'''
