# Defining Functions
def my_function():
    print("Hello")
    print("Bye")

my_function()

# While
# while something_is_ture
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Day6 Project: Escaping the Maze
# My codes
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if right_is_clear():
        turn_right()
    else:
        turn_left()
    while not right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_left()
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
 
 # Instructor's codes
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
