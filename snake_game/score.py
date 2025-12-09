from turtle import Turtle

POSITION_SCORE = (0,280)
POSITION_INFO = (0,-280)

HOME_POSITION = (0,0)
ALIGNMENT = "center"
FONT_SCORE = ("Arial", 14, "normal")
FONT_INFO = ("Arial", 10, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0

        with open("../../../Users/maria/OneDrive/Desktop/data.txt", "r") as file:
            self.highest = int(file.read())

        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.color("white")

        self.__write_score()

    def __write_score(self):
        self.goto(POSITION_INFO)
        self.write("To stop the game press the K key", align=ALIGNMENT, font=FONT_INFO)

        self.goto(POSITION_SCORE)
        self.write(f"Score: {self.points}    Highest Score: {self.highest}", align=ALIGNMENT, font=FONT_SCORE)

    def update(self):
        self.points += 1
        self.clear()
        self.__write_score()

    def end_game(self):
        self.goto(HOME_POSITION)
        self.write("Game Over!", align=ALIGNMENT, font=FONT_SCORE)

    def reset(self):
        if self.points > self.highest:
            self.highest = self.points

        self.points = 0
        self.clear()
        self.__write_score()

        with open("/Users/maria/OneDrive/Desktop/data.txt", "w") as file:
            file.write(str(self.highest))


