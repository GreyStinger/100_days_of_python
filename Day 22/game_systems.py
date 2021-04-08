import random
from turtle import Turtle

# Constants for PaddleCreate class
PADDLE_MOVEMENT = 20

# Constants for Scores class
ALIGNMENT = 'center'
FONT = ("Arial", 46, "normal")
X_DIST = 80
Y_DIST = 280


class Systems:
    """A systems class that will do everything from starting and stopping a match to clearing game fields"""
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
        if paddle_num == 0:
            self.goto(-540, 0)
        elif paddle_num == 1:
            self.goto(540, 0)
        else:
            raise Exception('Invalid Paddle Number')

    def up(self):
        self.goto(self.xcor(), self.ycor() + PADDLE_MOVEMENT)

    def down(self):
        self.goto(self.xcor(), self.ycor() - PADDLE_MOVEMENT)


class Ball(Turtle):
    """The ball, what more do you want (Super helpful docstring I know)"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fast')
        self.penup()
        self.shape('circle')
        self.heading_set()

    def heading_set(self):
        self.setheading(round(30 * (random.randint(0, 360) / 30)))

    def rebound_check(self):
        heading = self.heading()

        if  0 <= heading_set <= 90 or 180 <= heading_set <= 270:
            self.rebound_right(heading)
        elif 90 <= heading_set <= 180 or 270 <= heading_set <= 360:
            self.rebound_left(heading)


    # TODO make rebounds
    # Rebounds need to rebound at a controlled variable angle
    def rebound_right(self, heading):
        pass

    def rebound_left(self, heading):
        pass

    def move(self):
        if self.xcor() == 360 or self.xcor() == -360:
            self.rebound_check()

        self.forward(10)

    def reset(self):
        self.clear()
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
        self.draw_boarder()

    def draw_boarder(self):
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
        self.scores = (0, 0)
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

    def p_2_scored(self):
        self.scores[1] += 1
        self.write_scores()
