import turtle as t
from random import choice

import colorgram as cg

# Extract colors from an image
colors = cg.extract("image.jpg", 30)

# Create a list of RGB color tuples
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Set up the turtle
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Set up the screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Hirst Painting")

# Draw the dots
for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        tim.setposition(x, y)
        tim.dot(20, choice(rgb_colors))

screen.exitonclick()
