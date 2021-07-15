from turtle import Turtle, Screen, colormode
import random

kachua = Turtle()
s = Screen()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

kachua.pensize(5)
kachua.speed(9)
kachua.forward(10)
angles = [90, 180, 270, 90]
for _ in range(300):
    kachua.pencolor(random_color())
    kachua.right(random.choice(angles))
    kachua.forward(random.randint(25, 75))


s.exitonclick()