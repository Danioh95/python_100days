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
