from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-150, 250)
        self.color("black")
        self.hideturtle()
        self.update()

    def next_level(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"Level: {self.level}", font=FONT, align="center")
        self.goto(100, 250)
        self.write(f"Keys: \nUp: Move turtle up \nDown: Move turtle down", font=("Courier", 10, "normal"), align="left")

    def game_over(self):
        self.clear()
        self.goto(0,25)
        self.write(f"GAME OVER", font=("Courier", 21, "bold"), align="center")
        self.goto(0,-25)
        self.write(f"Maximum Level: {self.level}", font=("Courier", 21, "bold"), align="center")