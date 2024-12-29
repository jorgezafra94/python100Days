"""install pythonTurtle"""
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

screen = Screen()
screen.clear()

turtle = Turtle()
turtle.shape("turtle")
for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
