import turtle
from turtle import *
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cadetblue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


directions = [90, -90, 180, -180]

# for steps in range(15):
#     if steps % 2 == 0:
#         timmy.penup()
#     else:
#         timmy.pendown()
#     timmy.forward(steps - steps + 5)


# for _ in range(3):
#     timmy.forward(50)
#     timmy.right(360 / 3)
#     timmy.forward(50)
#
# for _ in range(4):
#     timmy.forward(50)
#     timmy.right(360 / 4)
#     timmy.forward(50)
#

# for i in range(3, 12):
#     for j in range(i):
#         timmy.forward(50)
#         timmy.right(360 / i)
#         timmy.forward(50)

# timmy.pensize(10)
# timmy.speed(10)
#
# for steps in range(200):
#     timmy.pencolor(random.choice(colours))
#     if steps % 2 == 0:
#         timmy.pendown()
#         timmy.right(random.choice(directions))
#
#     timmy.forward(20)

timmy.speed(10)

for i in range(72):
    timmy.pencolor(random.choice(colours))
    timmy.circle(100)
    timmy.right(i - i + 5)


screen = Screen()
screen.exitonclick()