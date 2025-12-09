from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("magenta")
        self.shapesize(0.5,0.5)
        self.speed("fastest")

        self.refresh_pos()

    def refresh_pos(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,260)

        self.goto(random_x,random_y)
