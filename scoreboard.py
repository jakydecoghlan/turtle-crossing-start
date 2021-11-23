from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition (-250, 270)
        self.color("black")
        self.level = 1
        self.write(f"Level {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align=ALIGN, font=FONT)


    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)