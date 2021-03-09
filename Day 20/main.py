from turtle import Turtle, Screen

snake = Turtle()
snake.speed('slow')
snake.color('white')
snake.shape('square')

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')

screen.exitonclick()
