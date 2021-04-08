import time
from turtle import Screen, Turtle

average_movement = 20
START_COORDINATES = ((0, 0), (-20, 0), (-40, 0), (-60, 0))


def snake_create(coords, heading=90.0):
    snake_section = Turtle()
    snake_section.penup()
    snake_section.color('green')
    snake_section.pensize(0)
    snake_section.speed('fast')
    snake_section.shape('square')
    snake_section.goto(coords)
    snake_section.setheading(heading)
    # snake_section.shapesize(outline=1)
    return snake_section


class Snake:
    def __init__(self):
        self.snake = [snake_create(coords) for coords in START_COORDINATES]
        self.play = True

    def new_snake(self):
        self.snake.append(snake_create(self.snake[-1].pos(), self.snake[-1].heading()))
        self.snake[-1].backward(average_movement)

    def right(self):
        self.snake[0].setheading(self.snake[0].heading() + 90)

    def left(self):
        self.snake[0].setheading(self.snake[0].heading() - 90)

    def move(self):
        for m in reversed(range(1, len(self.snake))):
            self.snake[m].goto(self.snake[m - 1].pos())
            self.snake[m].setheading(self.snake[m - 1].heading())

        self.snake[0].fd(average_movement)

        time.sleep(0.08)

    def end(self):
        self.play = False
