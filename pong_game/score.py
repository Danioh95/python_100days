from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.scoreboard = "Score: " + str(self.score)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(60, 260)
        self.write(self.scoreboard, align="center")

    def score(self):
        self.score += 1
