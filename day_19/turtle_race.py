from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

user_bet = ""
print(f"Please enter a color from the following list: {colors}")
while user_bet not in colors:
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
    ).lower().strip()

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Creating a finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.pensize(width=10)
finish_line.goto(x=220, y=190)
finish_line.pendown()
finish_line.goto(x=220, y=-190)

# The race
is_race_over = False
if user_bet:
    while not is_race_over:
        for turtle in all_turtles:
            if turtle.xcor() > 200 and not is_race_over:
                is_race_over = True
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    screen.title(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    screen.title(f"You've lost! The {winning_color} turtle is the winner!")

            if not is_race_over:
                turtle.forward(randint(0, 10))

screen.exitonclick()
