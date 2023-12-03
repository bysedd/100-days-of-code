import turtle
from random import randint

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

# Draw a spirograph
for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)

tim.screen.exitonclick()
