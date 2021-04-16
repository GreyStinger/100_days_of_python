import time
from turtle import Turtle

AVERAGE_MOVEMENT = 12
START_COORDINATES = ((0, 0), (-12, 0), (-24, 0), (-36, 0))
AVERAGE_SLEEP = 0.1


def snake_create(coords, heading=90.0):
    snake_section = Turtle()
    snake_section.shapesize(0.5)
    snake_section.penup()
    snake_section.color('green')
    snake_section.pensize(0)
    snake_section.speed('fast')
    snake_section.shape('square')
    snake_section.goto(coords)
    snake_section.setheading(heading)
    return snake_section


class Snake:
    def __init__(self):
        self.snake = [snake_create(coords) for coords in START_COORDINATES]
        self.snake_head = self.snake[0]
        self.died = False
        self.quit = False

    def new_snake(self):
        self.snake.append(snake_create(self.snake[-1].pos(), self.snake[-1].heading()))
        self.snake[-1].backward(AVERAGE_MOVEMENT)

    def right(self):
        self.snake_head.setheading(self.snake_head.heading() + 90)

    def left(self):
        self.snake_head.setheading(self.snake_head.heading() - 90)

    def move(self):
        for m in reversed(range(1, len(self.snake))):
            self.snake[m].goto(self.snake[m - 1].pos())
            self.snake[m].setheading(self.snake[m - 1].heading())

        self.snake_head.fd(AVERAGE_MOVEMENT)

        time.sleep(AVERAGE_SLEEP)

    def end(self):
        self.quit = True
