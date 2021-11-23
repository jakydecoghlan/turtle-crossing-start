import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

all_the_cars = []

manager = CarManager()
manager.hideturtle()

turtle = Player()
screen.listen()
screen.onkeypress(turtle.move, "Up")

scoreboard = Scoreboard()

times = 0
game_is_on = True
velocidad = 5

while game_is_on:
    times += 1
    time.sleep(0.1)
    screen.update()
    if times % 6 == 0:
        new_car = manager.car_creator()
        all_the_cars.append(new_car)
    for car in all_the_cars:
        car.cars_move(velocidad)
        if turtle.distance(car) < 20:   ###Collision
            scoreboard.game_over()
            game_is_on = False
    if turtle.ycor() > 280:
        turtle.new_level()
        scoreboard.level_up()
        velocidad += 10


screen.exitonclick()
