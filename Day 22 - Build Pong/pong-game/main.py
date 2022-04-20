from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game made by omerdikyol")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Creating middle dashed line
middle_line = Turtle()
middle_line.color("white")
middle_line.penup()
middle_line.hideturtle()
middle_line.goto(0, 300)
middle_line.setheading(270)
while middle_line.ycor() > -300:
    middle_line.pendown()
    middle_line.forward(75/2)
    middle_line.penup()
    middle_line.forward(25/2)

def go_up():
    new_y = l_paddle.ycor() + 20
    l_paddle.goto(l_paddle.xcor(), new_y)


def go_down():
    new_y = l_paddle.ycor() - 20
    l_paddle.goto(l_paddle.xcor(), new_y)


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game = True



while game:
    time.sleep(.01)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(l_paddle) < 38 or ball.distance(r_paddle) < 38 and abs(ball.xcor()) > 330:
        ball.bounce_x()
        ball.inc_speed(.5)

    # Detect if paddles misses
    if abs(ball.xcor()) > 380:
        if ball.xcor() > 0:
            scoreboard.l_score += 1
        else:
            scoreboard.r_score += 1
        ball.reset_position()
        scoreboard.update()
        if scoreboard.game_finished(5):
            game = False

screen.exitonclick()
