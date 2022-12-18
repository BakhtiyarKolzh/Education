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

def massive_by_row(length):
    num = 2
    turtle.speed(10)
    for i in range(5):
        create_houses(length)

        turtle.penup()
        turtle.home()
        turtle.right(90)
        turtle.forward(length*num)
        turtle.left(90)
        num +=2
        turtle.pendown()

def create_houses(length):
    count=1
    for i in range(5):
        for i in range(4):
            turtle.forward(length)
            turtle.right(90)

        turtle.left(45)
        turtle.forward(length * math.sqrt(0.5))
        turtle.right(90)
        turtle.forward(length * math.sqrt(0.5))
        turtle.left(45)

        turtle.penup()
        turtle.forward(10)
        count+=1
        turtle.pendown()


massive_by_row(20)
turtle.exitonclick()









