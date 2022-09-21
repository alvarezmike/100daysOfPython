from turtle import Turtle, Screen
import random

t = Turtle()
Screen().colormode(255)
t.shape("arrow")
t.speed("fastest")

r = 0
g = 0
b = 0


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r,g,b)


for _ in range(100):
    t.color(color())
    t.circle(100)
    t.left(_ + 1)
screen = Screen()
screen.exitonclick()