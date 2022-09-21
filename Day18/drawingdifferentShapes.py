from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")

for triangle in range(3):
    timmy_the_turtle.color("green")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(120)

for square in range(4):
    timmy_the_turtle.color("blue3")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

for pentagon in range(5):
    timmy_the_turtle.color("brown")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(72)

for hexagon in range(6):
    timmy_the_turtle.color("blue")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(60)

for heptagon in range(7):
    timmy_the_turtle.color("black")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(51.43)

for octagon in range(8):
    timmy_the_turtle.color("red")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(45)

for nonagon in range(9):
    timmy_the_turtle.color("purple")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(40)

for decagon in range(10):
    timmy_the_turtle.color("orange")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(36)


screen = Screen()
screen.exitonclick()
