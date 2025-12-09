import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from lives import Lives
import tkinter as tk

def chosen_no():
    pass

def chosen_yes():
    pass

def create_window():
    window = tk.Tk()
    window.title("You lost!")
    window.geometry("300x150")

    #add the question text
    label = tk.Label(window, text="Do you want to continue the game?")
    label.pack(pady=20)

    #create the frame for the buttons
    frame = tk.Frame(window)
    frame.pack()

    #create the buttons and place them in the created frame
    button_yes = tk.Button(frame, text="Yes (pay 20 coins)",command=chosen_yes,width=10)
    button_yes.pack(side="left",padx=10)

    button_no = tk.Button(frame, text="No",command=chosen_no,width=10)
    button_no.pack(side="right",padx=10)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
cars = CarManager()
score = Scoreboard()
lives = Lives()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # detects if the player has reached the top
    if player.has_finished():
        player.rellocate()
        score.next_level()
        cars.increment_speed()

    # detects the collision with a car
    if cars.collision_detected(player):
        if lives.enough_lives_left():
            lives.remove_life()
            player.rellocate()
        else:
            score.game_over()
            game_is_on = False

screen.exitonclick()