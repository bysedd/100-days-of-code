import turtle
from random import randint, choice


def random_color() -> tuple[float, float, float]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r / 255, g / 255, b / 255


tim = turtle.Turtle()
tim.speed("fastest")
tim.screen.bgcolor("black")
tim.pensize(10)

for _ in range(200):
    tim.color(random_color())
    tim.setheading(choice([0, 90, 180, 270]))
    tim.forward(30)

tim.screen.exitonclick()
