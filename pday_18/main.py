import random
import turtle as t

aria = 3

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_col = (r, g, b)
    return ran_col



tim.width(1)
tim.speed(30)
angles = [0, 90, 180, 270]

for _ in range(180):
    tim.right(5)
    tim.circle(100)
    tim.pencolor(random_color())

screen = t.Screen()
screen.exitonclick()

aria = 3
