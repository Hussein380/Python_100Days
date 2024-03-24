from turtle import Turtle, Screen

Tats = Turtle()
screen = Screen()


def move_forwards():
    Tats.forward(10)

def move_backwards():
    Tats.backward(10)


def turn_right():
    Tats.right(90)


def turn_left():
    Tats.left(90)


def clear():
    Tats.clear()
    Tats.penup()
    Tats.home()
    Tats.pendown()

screen.listen()
screen.onkey(move_forwards, "f")
screen.onkey(move_backwards, "b")
screen.onkey(turn_right, "r")
screen.onkey(turn_left, "l")
screen.onkey(clear, "c")

screen.mainloop()

screen.exitonclick()