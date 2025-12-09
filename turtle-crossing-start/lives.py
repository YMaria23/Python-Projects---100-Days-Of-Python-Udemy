from turtle import Turtle

START_POSITION = (140,263)
INCREMENT = 30
STARTING_NR_LIVES = 5

class Lives():
    def __init__(self):
        self.lives_left = 5
        self.position = START_POSITION
        self.lives = []
        self.__populate()

    def __life_init(self):
        new_life = Turtle()
        new_life.penup()
        new_life.shapesize(0.5,0.5)
        new_life.shape("circle")
        new_life.color("magenta")
        return new_life

    def __populate(self):
        self.position = START_POSITION
        for _ in range(STARTING_NR_LIVES):
            new_life = self.__life_init()
            new_life.goto(self.position)

            x_coord = self.position[0] + INCREMENT
            y_coord = self.position[1]
            self.position = (x_coord, y_coord)

            self.lives.append(new_life)

    def remove_life(self):
        self.lives_left -= 1
        self.lives[len(self.lives) - self.lives_left - 1].hideturtle()

    def enough_lives_left(self):
        return self.lives_left >= 2

