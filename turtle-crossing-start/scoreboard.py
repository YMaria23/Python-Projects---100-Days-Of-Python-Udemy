from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

        self.goto(-280,250)
        self.level = 1

        self.__write_level()

    def __write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.__write_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
