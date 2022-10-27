import colorgram as co
import turtle as t
import random

tim = t.Turtle()

colors = co.extract("paint.jpg", 30)
screen=t.Screen()

# list_co = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list_co.append(new_color)

color_list = [(198, 13, 32), (250, 237, 18), (39, 76, 189), (39, 217, 69), (229, 159, 45), (237, 225, 6), (28, 40, 156), (214, 76, 13), (198, 15, 11), (16, 154, 15), (242, 35, 165), (229, 17, 122), (71, 10, 31), (61, 15, 8), (224, 141, 208), (11, 97, 62), (51, 212, 230), (221, 160, 9), (18, 18, 43), (11, 227, 239), (238, 156, 218), (86, 75, 209), (80, 210, 159), (89, 233, 197), (59, 233, 241), (4, 68, 42)]
screen.colormode(255)

tim.penup()
tim.right(90)
tim.forward(250)
tim.right(90)
tim.forward(250)
tim.right(180)
tim.hideturtle()

print(random.choice(color_list))

def lines( self ):
    for _ in range(9):
        self.dot(20)
        self.forward(50)
        self.pencolor(random.choice(color_list))

for _ in range(5):
    lines(tim)
    tim.dot(20)
    tim.right(270)
    tim.forward(50)
    tim.right(270)
    lines(tim)
    tim.dot(20)
    tim.right(90)
    tim.forward(50)
    tim.right(90)




screen.exitonclick()