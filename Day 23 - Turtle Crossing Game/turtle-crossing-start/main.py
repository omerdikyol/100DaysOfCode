import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing made by omerdikyol")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False

    # Detect level finished
    if player.level_passed():
        player.reset_position()
        car_manager.next_level()
        scoreboard.next_level()

scoreboard.game_over()
screen.exitonclick()