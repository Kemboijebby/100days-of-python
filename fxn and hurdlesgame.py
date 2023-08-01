 #def my_function():
    #print("Anitah")
    #print("jebiwot")
#my_function()
turn_left=""
move=""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
at_goal=""
wall_in_front=""
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
#in the case of random hurdle heights
wall_on_right=""
def jump():
        turn_left()
        while wall_on_right():
            move()
            turn_right()
            move()
            turn_right()
            move()
        while front_is_clear():
            move()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
       