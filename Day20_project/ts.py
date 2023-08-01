from turtle import  Turtle,Screen
tim=Turtle()
tim.shape("square")


screen=Screen()
tim.penup()
tim.forward(20)
screen.listen()
screen.onkey(tim.up,"Up")
screen.onkey(tim.down,"Down")
screen.onkey(tim.left,"Left")




screen.exitonclick()
