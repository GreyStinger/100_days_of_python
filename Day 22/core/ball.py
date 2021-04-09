import random
from turtle import Turtle


class Ball(Turtle):
    """The ball, what more do you want (Super helpful docstring I know)"""

    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fast')
        self.penup()
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.heading_set()

    def heading_set(self):
        self.y_move = random.randint(8, 12)
        if random.randint(0, 2) == 1:
            self.y_move *= -1
        if random.randint(0, 2) == 1:
            self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def move(self):
        self.goto((self.xcor() + self.x_move), (self.ycor() + self.y_move))

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.heading_set()
