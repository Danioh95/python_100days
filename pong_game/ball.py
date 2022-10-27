import turtle as t
import random
inital_position = (0, 0)


class Ball():
    def __init__(self):
        self.ball = t.Turtle("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(inital_position)
        self.ball.setheading(45)
        self.ball.tilt(45)
        self.ball.wait = 0

    def moving(self):
        self.ball.forward(10)

    def rebounceu(self):
        head = self.ball.heading()
        if head == 45:
            self.ball.setheading(315)
        else:
            self.ball.setheading(225)

    def rebounceb(self):
        head = self.ball.heading()
        if head == 225:
            self.ball.setheading(135)
        else:
            self.ball.setheading(45)

    def rebounce1(self):
        head = self.ball.heading()
        if head == 225:
            self.ball.setheading(315)
        else:
            self.ball.setheading(45)

    def rebounce2(self):
        head = self.ball.heading()
        if head == 45:
            self.ball.setheading(135)
        else:
            self.ball.setheading(225)

    def score(self):
        self.ball.goto(0, 0)
        self.ball.wait = 100


