from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.turtlesize(40, 80)
        self.goto(pos)
        self.write(self.score, align="center", font=("Arial", 80, "normal"))

    def point(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Arial", 80, "normal"))
