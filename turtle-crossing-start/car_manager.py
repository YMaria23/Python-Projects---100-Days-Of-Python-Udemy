from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_CHANCE = 6


class CarManager:
    def __init__(self):
        self.cars = []
        self.normal_speed = STARTING_MOVE_DISTANCE
        self.chance = INITIAL_CHANCE

    def create_car(self):
        random_choice = random.randint(1,self.chance)

        if random_choice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            new_car.penup()
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_car.setheading(180)

            random_y = random.randint(-230, 230)

            new_car.goto(300, random_y)

            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.normal_speed)

    def increment_speed(self):
        self.normal_speed += MOVE_INCREMENT
        if self.chance != 3:
            self.chance -= 1

    def collision_detected(self,player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False

