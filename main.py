import random
import turtle as t
from turtle import Turtle, Screen
import colorgram

tim = Turtle()
t.colormode(255)
tim.shape("arrow")
tim.pd()
tim.pensize(2)
tim.teleport(0, y=None, fill_gap=False)
tim.ht()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


for i in range(0, 360, 5):
    tim.color(random_color())
    tim.circle(200)
    tim.setheading(i)













screen = Screen()
screen.title("This is my turtle")
screen.exitonclick()
