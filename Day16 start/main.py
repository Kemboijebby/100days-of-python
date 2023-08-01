# import another
# print(another.another_variable)

import turtle
#CREATING OBJECTS
#tinny=turtle.Turtle()
# from turtle import Turtle,screensize
# tinny=Turtle()
# print(tinny)


from prettytable import PrettyTable
x = PrettyTable()
x.add_column("pokeman Name",["pikachu","squirtle","charmander"])
x.add_column("Type",["Electric","Water","Fire"])
x.align = "l"

print(x)
