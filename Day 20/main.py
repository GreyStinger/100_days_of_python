from turtle import Screen, Turtle
import time

snake = []
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.mode('logo')
screen.tracer(0)

play = True


def main():
    global play

    def end():
        global play
        play = False

    def tl():
        snake[0].seth(snake[0].heading() - 90)

    def tr():
        snake[0].seth(snake[0].heading() + 90)

    def snake_create(co_ords):
        snake_section = Turtle()
        snake_section.pensize(10)
        snake_section.speed('fast')
        snake_section.color('white')
        snake_section.shape('square')
        snake_section.penup()
        snake_section.goto(co_ords)
        return snake_section

    screen.listen()

    snake.append(snake_create((0, 0)))
    snake.append(snake_create((-10, 0)))
    snake.append(snake_create((-20, 0)))

    while play:
        screen.onkeypress(key='a', fun=tl)
        screen.onkeypress(key='d', fun=tr)
        screen.onkeypress(key='s', fun=snake_create)

        for m in reversed(range(1, len(snake))):
            print(m)
            snake[m].goto(snake[m - 1].pos())

        snake[0].fd(10)
        time.sleep(0.05)
        screen.update()

        screen.onkeypress(key='Escape', fun=end)


if __name__ == '__main__':
    main()
