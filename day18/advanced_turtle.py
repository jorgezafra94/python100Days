from turtle import Turtle, Screen
import random


def random_color():
    return random.random(), random.random(), random.random()


t = Turtle()
t.speed(0)


def graphic_spirograph(size):
    for _ in range(size):
        t.color(random_color())
        t.circle(100)
        t.left(360 / size)


graphic_spirograph(100)
screen = Screen()
screen.exitonclick()
