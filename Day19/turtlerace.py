# turtle race bet game
from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("lightgrey")
screen.title("Turtle Race Bet")
# setup window height
screen.setup(width=500, height=400)
# ask user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
turtles = []
is_race_on = False

for color in colors:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y)
    y += 40
    turtles.append(new_turtle)


def create_vertical_line():
    line = Turtle()
    line.ht()
    line.color("black")
    line.pensize(4)
    line.penup()
    line.setposition(190, 140)
    line.pendown()
    line.right(90)
    line.forward(280)


create_vertical_line()

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in turtles:
        if turt.xcor() > 230:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You've won The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turt.forward(random_distance)

screen.exitonclick()