import turtle
import random

kachua = turtle.Turtle()
s = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

kachua.hideturtle()
kachua.speed(0)
kachua.setheading(225)
kachua.penup()
kachua.forward(300)
kachua.setheading(0)
kachua.pendown()


num_dots =  100
for count in range(1, num_dots + 1):
    kachua.pendown()
    kachua.dot(20, random_color())
    kachua.penup()
    kachua.forward(50)

    if count % 10 == 0:
        kachua.setheading(90)
        kachua.forward(50)
        kachua.setheading(180)
        kachua.forward(500)
        kachua.setheading(0)

s.exitonclick()