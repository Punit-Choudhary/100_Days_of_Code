from turtle import Turtle, Screen
import random

kachua = Turtle()
s = Screen()

colors = ["blue", "red", "purple", "green", "cyan", "violet", "brown"]

kachua.pensize(5)
kachua.speed(9)
kachua.forward(10)
angles = [90, 180, 270, 90]
for _ in range(300):
    kachua.pencolor(random.choice(colors))
    kachua.right(random.choice(angles))
    kachua.forward(random.randint(25, 75))


s.exitonclick()