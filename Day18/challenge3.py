from turtle import Turtle, Screen
import random

kachua = Turtle()
s = Screen()

colors = ['red', 'brown', 'blue', 'pink', 'violet', 'black']

for side in range(3, 10):
    angle = 360 // side
    kachua.pencolor(random.choice(colors))
    for _ in range(side):
        kachua.forward(100)
        kachua.right(angle)

s.exitonclick()