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
        self.goto(300, (random.randint(-250, 250)))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=1)
        # self.forward(STARTING_MOVE_DISTANCE)
        self.move_speed = STARTING_MOVE_DISTANCE


    def cars_move(self):
        self.forward(self.move_speed)

    def increment_speed(self):
        self.move_speed += MOVE_INCREMENT

