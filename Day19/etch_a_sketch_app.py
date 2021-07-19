from turtle import Turtle, Screen

kachua = Turtle()
screen = Screen()
screen.listen()

def moveforward():
    kachua.forward(10)

def movebackward():
    kachua.backward(10)

def moveleft():
    kachua.left(10)

def moveright():
    kachua.right(10)

def clear():
    kachua.reset()


screen.onkeypress(fun=moveforward, key="w")
screen.onkeypress(fun=movebackward, key="s")
screen.onkeypress(fun=moveleft, key="a")
screen.onkeypress(fun=moveright, key="d")
screen.onkeypress(fun=clear, key="c")

screen.exitonclick()