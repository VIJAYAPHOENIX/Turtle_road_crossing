from turtle import Screen
from player import Player
from score_board import  Score
from  car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
score = Score()
cars = CarManager()

screen.listen()
screen.onkey(player.move,"Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    score.update()

    cars.create_cars()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) <20:
            is_game_on = False
            player.game_over()

        if player.ending_point():
            score.level_up()
            player.starting_point()
            cars.level_up()


screen.exitonclick()