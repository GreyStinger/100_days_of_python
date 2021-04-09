import time
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 46, "normal")
X_DIST = 80
Y_DIST = 280


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
        time.sleep(2)
        self.write_scores()

    def p_2_scored(self):
        self.scores[1] += 1
        self.write_scores()
        self.p_score_screen(2)
        time.sleep(2)
        self.write_scores()

    def p_score_screen(self, player):
        self.goto(0, -40)
        if player == 1:
            self.write(arg=f'  Player {player} Scored!  ', move=False, align='left', font=FONT)
        else:
            self.write(arg=f'  Player {player} Scored!  ', move=False, align='right', font=FONT)
