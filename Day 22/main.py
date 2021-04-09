import time
from turtle import Screen

from core.ball import Ball
from core.border import Border
from core.game_systems import Systems
from core.paddle_create import PaddleCreate
from core.scores import Scores


def main():
    systems = Systems()

    screen = Screen()
    screen.tracer(0)
    screen.mode('logo')
    screen.setup(1200, 800)
    screen.bgcolor('#5eaaa8')
    screen.title('Pong')

    paddle = [PaddleCreate(n) for n in range(0, 2)]
    ball = Ball()
    border = Border()
    scores = Scores()

    border.draw_border()

    screen.listen()
    screen.onkeypress(key='w', fun=paddle[0].up)
    screen.onkeypress(key='s', fun=paddle[0].down)
    screen.onkeypress(key='Up', fun=paddle[1].up)
    screen.onkeypress(key='Down', fun=paddle[1].down)

    screen.onkeypress(key='Escape', fun=systems.stop)

    while systems.play:
        ball_y = ball.ycor()
        ball_x = ball.xcor()

        if ball_y > 344 or ball_y < -344:
            ball.bounce_y()

        if ball_x > 510 or ball_x < -510:
            if paddle[0].distance(ball) < 50 or paddle[1].distance(ball) < 50:
                ball.bounce_x()

        if ball_x > 550 or ball_x < -550:
            if ball_x > 550:
                scores.p_1_scored()
                for i in range(2):
                    paddle[i].reset()
            else:
                scores.p_2_scored()
                for i in range(2):
                    paddle[i].reset()

            ball.reset()

        ball.move()
        screen.update()

        time.sleep(ball.move_speed)


if __name__ == '__main__':
    main()
