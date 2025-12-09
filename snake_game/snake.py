from turtle import Screen, Turtle
import random
MOVING_DISTANCE = 20
SEGMENT_DISTANCE = 20

COLLISION_DISTANCE = 10

OUT_OF_SCREEN = (1000,1000)

INITIAL_POSITIONS = [(0,0),(0,-20),(0,-40)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        #create snake
        self.snake = []

        self.__create_snake()
        self.head = self.snake[0]

    def __create_snake(self):
        for position in INITIAL_POSITIONS:
            self.__add_segment(position)

    def __add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.speed("fastest")

        self.snake.append(new_turtle)

    def extend_snake(self):
        self.__add_segment(self.snake[-1].position())

    def collision_with_tail(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) < COLLISION_DISTANCE:
                return True
        return False

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(MOVING_DISTANCE)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def is_over(self):
        return self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280

    def start_new_position(self):
        for segment in self.snake:
            segment.goto(OUT_OF_SCREEN)

        self.snake.clear()
        self.__create_snake()
        self.head = self.snake[0]





