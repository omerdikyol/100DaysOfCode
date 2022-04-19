import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Challenge - Etch-A-Sketch App

# def move_forwards(): tim.forward(10)
# def move_backwards(): tim.forward(10)
# def turn_right(): tim.right(10)
# def turn_left(): tim.left(10)
# def clear():
#     tim.clear()
#     tim.home()
#
# screen.listen()
# turtle.onkey(key="w", fun=move_forwards)
# turtle.onkey(key="s", fun=move_backwards)
# turtle.onkey(key="d", fun=turn_right)
# turtle.onkey(key="a", fun=turn_left)
# turtle.onkey(key="c", fun=clear)


# Turtle Racing
screen.setup(width=500, height=400)
inp = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-70, -40, -10, 20, 50, 80]
is_race_on = True
racers = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_axis[i])
    racers.append(new_turtle)

while is_race_on:

    for turtle in racers:
        if turtle.xcor() > 230:     # x coordinate of turtle
            winner = turtle.pencolor()

            if winner == inp.lower(): print(f"You've won! The {winner} turtle is winner!")
            else: print(f"You've lost! The {winner} turtle is winner!")
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()
