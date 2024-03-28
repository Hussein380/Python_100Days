import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move()

    #Detect collision
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    #Detect a successfull crossing
    if player.Is_at_finish():
        player.goto_start()
        carmanager.level_up()
        scoreboard.increase_level()


    


screen.exitonclick()

