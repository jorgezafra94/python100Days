from turtle import Turtle, Screen
import random


t = Turtle()
t.home()
for i in range(3, 10):
    R, G, B = random.random(), random.random(), random.random()
    t.color((R, G, B))
    degrees = 360 / i
    for j in range(i):
        t.forward(100)
        t.right(degrees)

screen = Screen()
screen.exitonclick()