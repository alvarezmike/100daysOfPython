import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Safely")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# move turtle
screen.onkey(player.move_up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect player cross successfully
    if player.player_crosses():
        player.return_starting_position()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()