from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.update()

    def update(self):
        self.clear()
        self.goto(-290, 270)
        self.write(f"Highscore: {self.high_score}", align="left", font=("Courier", 10, "normal"))
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 270)
        self.write(f"Keys: Up,Down,Left,Right", align="left", font=("Courier", 10, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                self.high_score = self.score
                file.write(f"{self.score}")
        self.score = 0
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)