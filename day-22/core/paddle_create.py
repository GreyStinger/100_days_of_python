from turtle import Turtle

PADDLE_MOVEMENT = 25


class PaddleCreate(Turtle):
    """A turtle graphics class that creates and moves the paddles in the game"""

    def __init__(self, paddle_num):
        super().__init__()
        self.color('white')
        self.speed('fast')
        self.penup()
        self.setheading(0)
        self.shape('square')
        self.shapesize(stretch_len=5.8, stretch_wid=0.8)
        self.paddle_num = paddle_num
        self.position()

    def up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + PADDLE_MOVEMENT)

    def down(self):
        if self.ycor() > -300:
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVEMENT)

    def reset(self):
        self.position()

    def position(self):
        if self.paddle_num == 0:
            self.goto(-540, 0)
        elif self.paddle_num == 1:
            self.goto(540, 0)
        else:
            raise Exception('Invalid Paddle Number')
