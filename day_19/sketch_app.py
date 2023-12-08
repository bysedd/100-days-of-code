from functools import partial
from turtle import Turtle, Screen


def move(turtle: Turtle, direction: int, distance: int = 20):
    match direction:
        case "forward":
            turtle.forward(distance)
        case "backward":
            turtle.backward(distance)
        case "left":
            turtle.setheading(turtle.heading() + distance)
        case "right":
            turtle.setheading(turtle.heading() - distance)


screen = Screen()
tim = Turtle()

actions = {'w': 'forward', 's': 'backward', 'a': 'left', 'd': 'right'}

screen.listen()
for key, action in actions.items():
    screen.onkey(key=key, fun=partial(move, tim, action))
screen.onkey(key="c", fun=tim.clear)

screen.exitonclick()
