from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game made by omerdikyol")
screen.tracer(0)

snake = Snake()
food = Food()
sboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True

while game:
    screen.update()
    time.sleep(.05)
    snake.move()

    # Detect collision with food
    if food.distance(snake.head) < 15:
        food.refresh()
        sboard.increase_score()
        snake.extend()

    # Detect collision with wall
    snake.pass_wall(600)

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sboard.reset()
            snake.reset()

screen.exitonclick()
