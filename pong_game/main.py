import turtle as t
from paddles import Paddle, startin_position1, startin_position2, Line
import time
from ball import Ball
from Scoreboard import Scoreboard


screen = t.Screen()
screen.setup(1200, 700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

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




paddle1 = Paddle(startin_position1)
paddle2 = Paddle(startin_position2)
balla = Ball()
line = Line()
scores = Scoreboard((-75, 210))
scores2 = Scoreboard((75, 210))


screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    balla.ball.wait -= 1
    if balla.ball.wait < 70:
        balla.moving()


    for i in range(len(paddle1.segments)):
        if balla.ball.distance(paddle1.segments[i]) < 20:
            balla.rebounce1()

        elif balla.ball.distance(paddle2.segments[i]) < 20:
            balla.rebounce2()
    if balla.ball.ycor() > 340:
        balla.rebounceu()

    if balla.ball.ycor() < -340:
        balla.rebounceb()

    if balla.ball.xcor() > 600:
        balla.score()
        scores.point()

    if balla.ball.xcor() < -600:
        balla.score()
        scores2.point()


screen.exitonclick()
