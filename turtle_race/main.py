from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

initial_pos_x = -230
initial_pos_y = -100

def set_pos(current_turtle,position_x,position_y):
    current_turtle.penup()
    current_turtle.goto(position_x,position_y)

def go_forward_random(current_turtle):
    random_distance = random.randint(0,10)
    current_turtle.forward(random_distance)

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    set_pos(new_turtle,initial_pos_x,initial_pos_y)

    initial_pos_y = initial_pos_y + 40

    turtles.append(new_turtle)

continue_race = True
while continue_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The winner is the {winning_turtle} turtle.")
            else:
                print(f"You've lost! The winner is the {winning_turtle} turtle.")
            continue_race = False
        go_forward_random(turtle)

screen.exitonclick()