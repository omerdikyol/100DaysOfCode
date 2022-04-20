from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(250,250)
        self.write(f"Keys: \nLeft Paddle: W and S\nRight Paddle: Up and Down")
        self.goto(-390,280)
        self.write(f"First person to reach five wins", )

    def game_finished(self, win_point):
        if self.l_score == win_point or self.r_score == win_point:
            self.goto(0, 0)
            self.write("GAME FINISHED", align="center", font=("Courier", 40, "normal"))
            return True
