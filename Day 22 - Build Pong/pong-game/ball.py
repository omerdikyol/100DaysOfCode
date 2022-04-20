from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.ball_speed_x = 3.2
        self.ball_speed_y = 3.2

    def move(self):
        self.goto(self.xcor() + self.ball_speed_x, self.ycor() + self.ball_speed_y)

    def bounce_y(self):
        self.ball_speed_y *= -1

    def bounce_x(self):
        self.ball_speed_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def inc_speed(self, const):
        self.ball_speed_y += const
        self.ball_speed_x += const
