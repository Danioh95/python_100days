import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Choose your color: ")
all_turtle = []
race_on = False

def initial(colora, y, clas):
    clas = Turtle("turtle")
    clas.color(colora)
    clas.penup()
    clas.goto(-230, y)
    all_turtle.append(clas)


if user_bet:
    race_on = True



initial("red", -80, "tim")
initial("blue", -40, "tom")
initial("gold", 0, "rom")
initial("green", 40, "som")
initial("violet", 80, "tol")

while race_on:
    for all in all_turtle:
        fast = random.randint(0, 10)
        all.forward(fast)
        if all.pos()[0] > 230:
            race_on = False
            if all == user_bet:
                print("Congratulation, you win")
            else:
                print(f"Your {all.color()[0]} turtle didn't win")
            break
screen.exitonclick()
