import turtle
from random import randint

tim = turtle.Turtle()
tim.speed(5)
tim.screen.bgcolor("black")


def random_color() -> tuple[float, float, float]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r / 255, g / 255, b / 255


for sides in range(4, 11):
    angle = 360 / sides
    tim.pencolor(random_color())
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

turtle.exitonclick()
