import time
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = None
        self.color('white')
        self.speed('fast')
        self.hideturtle()
        self.penup()
        self.set_all()

    def draw_score(self):
        self.goto(0, 226)
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.draw_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)
        time.sleep(4)

    def quite_game(self):
        self.goto(0, 0)
        self.write(arg='GOODBYE THEN', move=False, align=ALIGNMENT, font=FONT)
        time.sleep(4)

    def set_all(self):
        self.clear()
        self.score = 0
        self.draw_score()
