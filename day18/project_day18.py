import random
from turtle import Turtle, Screen

import colorgram


def get_colors_from_image(img):
    colors = colorgram.extract(img, 20)
    clean_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        clean_colors.append((r, g, b))
    return clean_colors


def set_window_properties(window):
    window.setup(width=550, height=550, startx=0, starty=0)
    window.setworldcoordinates(0, 0, 500, 500)
    window.colormode(255)


def create_picture(turtle, colors):
    turtle.penup()
    turtle.speed("fastest")
    turtle.hideturtle()
    for i in range(0, 450, 50):
        turtle.setposition(50, i + 50)
        for _ in range(0, 450, 50):
            random_color_tuple = random.choice(colors)
            turtle.dot(20, random_color_tuple)
            turtle.forward(50)
        turtle.penup()


image = 'image.jpg'
colors_list = get_colors_from_image(image)
t = Turtle()
screen = Screen()
set_window_properties(screen)

create_picture(t, colors_list)

screen.exitonclick()
