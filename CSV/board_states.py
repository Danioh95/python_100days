from turtle import Turtle

class states_names(Turtle):

    def __init__(self, pos, states):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.turtlesize(10, 10)
        self.goto(pos)
        self.write(states, align="center", font=("Arial", 10, "normal"))