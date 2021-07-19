import turtle
import random


screen = turtle.Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False
colors = ["red", "green", "blue", "yellow", "pink", "orange"]
y_axis = [-100, -60, -20, 20, 60, 100]
kachue = []


for i in range(0, 6):
    kachua = turtle.Turtle(shape="turtle")
    kachua.penup()
    kachua.color(colors[i])
    kachua.goto(x=-230, y=y_axis[i])
    kachue.append(kachua)

if user_bet:
    is_race_on = True

while is_race_on:
    for kachua in kachue:
        if kachua.xcor() > 230:
            is_race_on = False
            winner = kachua.pencolor()
            if winner == user_bet:
                print(f"You've won 🎉. The {winner} color turtle 🐢 won the race!")
            else:
                print(f"You've lost. The {winner} color turtle 🐢 won the race!")
        kachua.forward(random.randint(0, 10))

screen.exitonclick()
