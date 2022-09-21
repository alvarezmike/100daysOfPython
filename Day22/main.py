from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setting screen features.
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# init paddles from Paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# creating ball from Ball class
ball = Ball()

scoreboard = Scoreboard()


screen.listen()
# right paddle movement on key
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
# lef paddle movement on key.
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

GAME_OVER = 7
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == GAME_OVER:
        winner = "Left Player"
        scoreboard.end(winner)
        game_is_on = False

    elif scoreboard.r_score == GAME_OVER:
        winner = "Right Player"
        scoreboard.end(winner)
        game_is_on = False


screen.exitonclick()