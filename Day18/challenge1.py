from turtle import Turtle, Screen

kachua = Turtle()
screen = Screen()

for _ in range(4):
    kachua.forward(100)
    kachua.right(90)

screen.exitonclick()
