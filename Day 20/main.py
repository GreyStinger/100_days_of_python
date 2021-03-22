from turtle import Screen
import snake as s

snake = s.Snake()


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


window = window(left=snake.left, right=snake.right, new=snake.new_snake, end=snake.end)


def main():
    while snake.play:
        snake.move()


if __name__ == '__main__':
    main()
