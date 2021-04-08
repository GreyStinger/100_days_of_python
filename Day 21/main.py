from turtle import Screen
import snake as s
import food as f


def main():
    def window():
        window_mk = Screen()
        window_mk.tracer(0)
        window_mk.setup(width=440, height=440)
        window_mk.bgcolor('black')
        window_mk.title('Snake')
        window_mk.mode('logo')
        return window_mk

    screen = window()

    snake = s.Snake()
    food = f.Food()

    screen.listen()
    screen.onkeypress(key='a', fun=snake.left)
    screen.onkeypress(key='d', fun=snake.right)
    screen.onkeypress(key='s', fun=snake.new_snake)
    screen.onkeypress(key='Escape', fun=snake.end)

    screen.update()

    while snake.play:
        snake.move()

        if snake.snake_head.distance(food) <= 2:
            food.food_repos()
            snake.new_snake()

        screen.update()


if __name__ == '__main__':
    main()
