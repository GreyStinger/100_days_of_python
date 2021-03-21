import time
from turtle import Screen, Turtle

average_movement = 20


def snake_create(coords, heading=90.0):
    snake_section = Turtle()
    snake_section.pensize(0)
    snake_section.speed('fast')
    snake_section.color('white')
    snake_section.shape('square')
    snake_section.penup()
    snake_section.goto(coords)
    snake_section.setheading(heading)
    snake_section.color('green')
    snake_section.shapesize(outline=1)
    return snake_section


def window(left, right, new, end):
    screen = Screen()
    screen.listen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake')
    screen.mode('logo')
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(key='a', fun=left)
    screen.onkeypress(key='d', fun=right)
    screen.onkeypress(key='s', fun=new)
    screen.onkeypress(key='Escape', fun=end)
    return screen


class Snake:
    def __init__(self):
        self.window = window(left=self.left, right=self.right, new=self.new_snake, end=self.end)
        self.snake = [snake_create((0, 0)), snake_create((-20, 0)), snake_create((-40, 0)),
                      snake_create((-60, 0))]
        self.play = True

    def new_snake(self):
        self.snake.append(snake_create(self.snake[-1].pos(), self.snake[-1].heading()))
        self.snake[-1].backward(average_movement)

    def right(self):
        self.snake[0].setheading(self.snake[0].heading() + 90)

    def left(self):
        self.snake[0].setheading(self.snake[0].heading() - 90)

    def run(self):

        while self.play:
            for m in reversed(range(1, len(self.snake))):
                self.snake[m].goto(self.snake[m - 1].pos())

            self.snake[0].fd(average_movement)

            time.sleep(0.08)

            self.window.update()

    def end(self):
        self.play = False
