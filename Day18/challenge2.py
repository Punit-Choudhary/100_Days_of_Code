from turtle import Screen, Turtle

kachua = Turtle()
s = Screen()

for _ in range(10):
    kachua.forward(10)
    kachua.penup()
    kachua.forward(10)
    kachua.pendown()

s.exitonclick()
