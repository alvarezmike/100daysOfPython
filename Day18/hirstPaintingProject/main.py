# import colorgram
# 18/100 days of Python
# The Project challenge is to replicate a Hirst painting.
# using the Turtle and Colorgram packages.
# 10 x 10 dots painting.
from turtle import Turtle, Screen, colormode
import random
# The following lines purpose is to extract colors of a jpg.

# rgb_colors = [] # empty list
# #extract 25 color from an image
# colors = colorgram.extract("image.jpg", 25)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82), (207, 202, 146), (144, 176, 161), (178, 150, 156), (176, 202, 188), (217, 179, 172), (22, 77, 93)]
d = Turtle()
d.speed("fastest")
d.penup()
d.goto(-200,-300)
colormode(255)


def upwards_fromRight():
    d.setheading(90)
    d.forward(50)
    d.setheading(180)
    d.forward(50)


def upwards_fromLeft():
    d.setheading(90)
    d.forward(50)
    d.setheading(0)
    d.forward(50)


def left():
    for l in range(10):
        d.dot(20, random.choice(color_list)) # size of dot , and color choice
        d.hideturtle() # hide drawing process
        d.penup() # hide lines
        d.forward(50) # move by 50


def right():
    for z in range(10):
        d.dot(20, random.choice(color_list)) # size of dot , and color choice
        d.hideturtle() # hide drawing process
        d.penup() # hide lines
        d.forward(50) # move by 50


stop = True
while stop:
    for i in range(5):
        right()
        upwards_fromRight()
        left()
        upwards_fromLeft()
        if i % 10 == 0:
            stop = False


screen = Screen()
screen.exitonclick()