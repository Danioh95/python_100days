import turtle as t

startin_position1 = [(-500, -30), (-500, -10), (-500, 10), (-500, 30)]
startin_position2 = [(500, -30), (500, -10), (500, 10), (500, 30)]


class Paddle():
    def __init__(self, starting_position):
        self.segments = []
        self.create_paddle(starting_position)

    def create_paddle(self, startin_position_c):
        for position in startin_position_c:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        for i in range(len(self.segments)):
            self.segments[i].setheading(90)
            if self.segments[3].ycor() < 350:
                self.segments[i].forward(20)

    def down(self):
        for i in range(len(self.segments)):
            self.segments[i].setheading(270)
            if self.segments[3].ycor() > -290:
                self.segments[i].forward(20)


startin_position = []
x = -300
for i in range(21):
    startin_position.append((0, x))
    x += 30


class Line(t.Turtle):
    def __init__(self):
        self.segments = []
        self.create_line()

    def create_line(self):
        for position in startin_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(0.8, 0.3)
        new_segment.goto(position)
        self.segments.append(new_segment)
