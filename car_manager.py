from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0, 5)])
        self.penup()
        self.setheading(180)
        self.goto(300, (random.randint(-230, 230)))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=5)
        self.move_speed = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def car_creator(self):
        self.car = CarManager()
        return self.car

    def cars_move(self, velocidad):
        self.forward(velocidad)

    # def level_up(self):
    #     self.move_speed += self.move_increment



