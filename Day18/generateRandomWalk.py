from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

colours = ["medium aquamarine", "purple", "tomato", "spring green", "dodger blue", "wheat", "red", "SlateGray"]
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
