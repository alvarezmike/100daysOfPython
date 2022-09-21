from turtle import Turtle, Screen
# Etch-A-Sketch App

tim = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")
# activates key pressing
screen.listen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear():
    tim.reset()

# when user press defined key, trigger function.

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()