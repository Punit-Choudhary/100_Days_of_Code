import turtle
import random

kachua = turtle.Turtle()
s = turtle.Screen()
kachua.speed(13)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def draw_rangoli(size):
    for i in range(360 // size):
        kachua.pencolor(random_color())
        kachua.circle(100)
        kachua.left(size)

draw_rangoli(7)

s.exitonclick()