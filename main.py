import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
all_the_cars = []
manager = CarManager()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.car_creator()
    screen.ontimer(car_creator(), 1000)
    all_the_cars.append(car_creator())
    for car in all_the_cars:
        car_creator().cars_move()
