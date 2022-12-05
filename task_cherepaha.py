import turtle

"""
# Arrow
turtle.forward(100)
turtle.done()

"""
########################################################################################################################
# Spiral
"""
deg = 30
size = 100
turtle.pendown()

for i in range(1,50):
    turtle.forward(size-i)
    turtle.left(deg)

turtle.done()
"""
########################################################################################################################
########################################################################################################################
"""
# Kvadrat

deg = 90
size = 100
turtle.pendown()

for i in range(8):
    turtle.forward(size)
    turtle.left(deg)
turtle.done()
"""
########################################################################################################################
# turtle.pendown()
# turtle.forward(size)
#
# turtle.left(deg)
# turtle.forward(size)
#
# turtle.left(deg)
# turtle.forward(size)
#
# turtle.left(deg)
# turtle.forward(size)
#
# turtle.done()
########################################################################################################################
########################################################################################################################
"""

deg = 30
size = 100
turtle.pendown()
turtle.speed(60)

for i in range(1,50):
    turtle.forward(size-i)
    turtle.left(deg)

turtle.penup()
turtle.home()


turtle.pendown()
for i in range(1,50):
    turtle.forward(size-i)
    turtle.right(deg)

turtle.done()
"""
########################################################################################################################
########################################################################################################################
import math


def drawHouse(turtle, length):
    for i in range(2):
        turtle.speed(10)
        turtle.pensize(5)

        for i in range(4):
            turtle.forward(length)
            turtle.right(90)

        turtle.left(45)
        turtle.forward(length * math.sqrt(2))
        turtle.right(90)
        turtle.forward(length * math.sqrt(2))
        turtle.right(135)
        for i in range(4):
            turtle.forward(length)
            turtle.left(90)

    drawHouse(turtle,80)

    turtle.done()
####dfsdfsf

