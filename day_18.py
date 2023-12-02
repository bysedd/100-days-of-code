import turtle
from random import randint, choice

tim = turtle.Turtle()
tim.screen.colormode(255)


def random_color() -> tuple[float, float, float]:
    """
    Generates random RGB color values.

    :return: A tuple of three float values representing the RGB color values.
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


tim.speed("fastest")
tim.screen.bgcolor("black")
tim.pensize(10)

for _ in range(200):
    tim.color(random_color())
    tim.setheading(choice([0, 90, 180, 270]))
    tim.forward(30)

tim.screen.exitonclick()
