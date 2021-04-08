import time
from turtle import Screen

from game_systems import Systems, PaddleCreate, Ball, Border, Scores


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

    screen.listen()
    screen.onkeypress(key='w', fun=paddle[0].up)
    screen.onkeypress(key='s', fun=paddle[0].down)
    screen.onkeypress(key='Up', fun=paddle[1].up)
    screen.onkeypress(key='Down', fun=paddle[1].down)

    screen.onkeypress(key='Escape', fun=systems.stop)

    while systems.play:
        ball.move()

        screen.update()
        time.sleep(0.05)


if __name__ == '__main__':
    main()
