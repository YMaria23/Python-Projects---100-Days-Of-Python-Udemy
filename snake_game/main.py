import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Best Snake Game :)")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

continue_game = True

def stop_game():
    global continue_game
    continue_game = False
    score.end_game()

screen.onkey(stop_game,"k")

while continue_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detects collisions with food
    if snake.head.distance(food) < 15:
        food.refresh_pos()
        score.update()
        snake.extend_snake()

    #detects collision with wall
    if snake.is_over():
        score.reset()
        snake.start_new_position()

    #detect collision with tail
    if snake.collision_with_tail():
        score.reset()
        snake.start_new_position()

screen.exitonclick()