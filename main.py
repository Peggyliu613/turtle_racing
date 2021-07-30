from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y = 60
for i in range(6):
    shu = Turtle("turtle")
    shu.color(colors[i])
    shu.penup()
    shu.goto(-200, y)
    y -= 30
    turtles.append(shu)


start_race = False

bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")


if bet:
    start_race = True


while start_race:
    for turtle in turtles:
        turtle.forward(random.randint(0, 5))
        if turtle.xcor() >= 200:
            winning_color = turtle.pencolor()
            start_race = False
            break

if winning_color == bet:
    print("You win!")
else:
    print(f"You lose! The winning color is the {winning_color} turtle")


screen.exitonclick()
