from turtle import Turtle,Screen
import random
s=Turtle()
colors=["red","black","dark red","firebrick","green","blue","deep pink"]
def draw_shape(num_sides):
    angle=360 / num_sides
    for i in range(num_sides):
        s.forward(100)
        s.right(angle)

for shape_side_n in range(3,11):
    s.color(random.choice(colors))
    draw_shape(shape_side_n)




screen=Screen()
screen.exitonclick()