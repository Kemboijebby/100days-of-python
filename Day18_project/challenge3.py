# import random
# from turtle import Turtle,Screen
# tim=Turtle()
# colors=["red","black","dark red","firebrick","green","blue","deep pink"]
#
# for i in range(10):
#     tim.shape("circle")
#     tim.forward()

#from turtle import Turtle,Screen
# tim=Turtle()
# tim.penup()
# for i in range(1, 500, 50):
#     tim.right(90)  # Face South
#     tim.forward(i)  # Move one radius
#     tim.right(270)  # Back to start heading
#     tim.pendown()  # Put the pen back down
#     tim.circle(i)  # Draw a circle
#     tim.penup()  # Pen up while we go home
#     tim.home()
import  random
import  turtle as t
tim=t.Turtle()
t.colormode(255)
directions=[0,90,180,270]
def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    random_color=(r,g,b)
    return random_color
tim.pensize(10)
tim.speed(0)
for i in range(200):
    tim.setheading(random.choice(directions))
    tim.forward(30)
    tim.color(random_color())


screen=t.Screen()
screen.exitonclick()