from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
def move_forwards():
    tim.forward(100)
def move_backwards():
    tim.back(100)
def move_counter_clockwise():
    tim.left(10)
def move_clockwise():
    tim.right(-10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="W",fun=move_forwards)
screen.onkey(key="S",fun=move_backwards)
screen.onkey(key="A",fun=move_counter_clockwise)
screen.onkey(key="D",fun=move_clockwise)
screen.onkey(key="C",fun=clear)
screen.exitonclick()