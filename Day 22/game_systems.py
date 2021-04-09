import random
import time
from turtle import Turtle

# Constants for PaddleCreate class
PADDLE_MOVEMENT = 25

# Constants for Scores class
ALIGNMENT = 'center'
FONT = ("Arial", 46, "normal")
X_DIST = 80
Y_DIST = 280


class Systems:
    """A systems class monitors gameplay"""
    def __init__(self):
        self.play = True

    def stop(self):
        self.play = False


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


class Ball(Turtle):
    """The ball, what more do you want (Super helpful docstring I know)"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fast')
        self.penup()
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.heading_set()

    def heading_set(self):
        self.y_move = random.randint(8, 12)
        if random.randint(0, 2) == 1:
            self.y_move *= -1
        if random.randint(0, 2) == 1:
            self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        
    def move(self):
        self.goto((self.xcor() + self.x_move), (self.ycor() + self.y_move))

    def reset(self):
        self.goto(0, 0)
        self.heading_set()


class Border(Turtle):
    """A turtle graphics subclass that draws the border for a Ping Pong field automatically"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fast')
        self.color('white')
        self.penup()
        self.goto(-563, 363)
        self.pendown()
        self.setheading(90)
        self.pensize(6)

    def draw_border(self):
        for _ in range(2):
            self.forward(1126)
            self.setheading(self.heading() + 90)
            self.forward(100)
            self.penup()
            self.forward(526)
            self.pendown()
            self.forward(100)
            self.setheading(self.heading() + 90)

        self.penup()
        self.goto(0, 366)
        self.setheading(180)

        self.forward(18)

        for i in range(12):
            self.pendown()
            self.forward(30)
            self.penup()
            if i != 11:
                self.forward(30)
            else:
                self.forward(18)


class Scores(Turtle):
    """Keeps track of game scores"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fast')
        self.hideturtle()
        self.penup()
        self.scores = [0, 0]
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.goto(-X_DIST, Y_DIST)
        self.write(arg=self.scores[0], move=False, align=ALIGNMENT, font=FONT)
        self.goto(X_DIST, Y_DIST)
        self.write(arg=self.scores[1], move=False, align=ALIGNMENT, font=FONT)

    def p_1_scored(self):
        self.scores[0] += 1
        self.write_scores()
        self.p_score_screen(1)
        time.sleep(3)
        self.write_scores()

    def p_2_scored(self):
        self.scores[1] += 1
        self.write_scores()
        self.p_score_screen(2)
        time.sleep(3)
        self.write_scores()

    def p_score_screen(self, player):
        self.goto(0, -40)
        if player == 1:
            self.write(arg=f'  Player {player} Scored!  ', move=False, align='left', font=FONT)
        else:
            self.write(arg=f'  Player {player} Scored!  ', move=False, align='right', font=FONT)
