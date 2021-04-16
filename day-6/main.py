def turn_left():
    pass


def move():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def climb():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    climb()

