from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0,5)])
        self.penup()
        self.setheading(180)
        self.goto(300, (random.randint(-300, 300)))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=1)

        # self.ycor(random.randint(-300, 300))

    def car_creator():
        car = CarManager()
        return car

    def cars_move(self):
        self.forward(5)





