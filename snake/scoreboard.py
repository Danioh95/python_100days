from turtle import Turtle

with open("scor.txt") as file:
    higscore = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(higscore)
        self.scoreboard = "Score: " + str(self.score)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        else:
            pass
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.scoreboard} High Score: {self.high_score} ", align="center")
        with open("scor.txt", mode="w") as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center")

    def point(self):
        self.score += 1
        self.scoreboard = "Score: " + str(self.score)
        self.update_scoreboard()
