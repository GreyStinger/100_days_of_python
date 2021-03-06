from turtle import Screen

from core import food as f, boarder as b2, snake as s, scoreboard as b1


def main():
    def window():
        window_mk = Screen()
        window_mk.tracer(0)
        window_mk.setup(width=500, height=500)
        window_mk.bgcolor('black')
        window_mk.title('Snake')
        window_mk.mode('logo')
        return window_mk

    screen = window()
    snake = s.Snake()
    food = f.Food()
    board = b1.Scoreboard()
    boarder = b2.Boarder()

    boarder.draw_boarder()

    screen.listen()
    screen.onkeypress(key='a', fun=snake.left)
    screen.onkeypress(key='d', fun=snake.right)
    screen.onkeypress(key='Escape', fun=snake.end)

    while not snake.quit and not snake.died:
        snake.play = True
        snake.died = False
        while not snake.quit and not snake.died:
            screen.update()

            snake.move()

            if snake.snake_head.distance(food) <= 2:
                food.food_repos()
                snake.new_snake()
                board.score_up()

            if snake.snake_head.xcor() > 222 or snake.snake_head.ycor() > 222 or snake.snake_head.xcor() < -222 or \
                    snake.snake_head.ycor() < -222:
                snake.died = True

            for snake_segment in snake.snake[1:]:
                if snake.snake_head.distance(snake_segment) <= 0:
                    snake.died = True

        if snake.died:
            board.game_over()
        else:
            board.quite_game()


if __name__ == '__main__':
    main()
