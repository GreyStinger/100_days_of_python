from random import randint
from turtle import Turtle

ROUND_TO = 12


def find_location():
    return ROUND_TO * round(randint(-222, 222) / ROUND_TO), ROUND_TO * round(randint(-222, 222) / ROUND_TO)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.4)
        self.color('red')
        self.speed('fast')
        self.food_repos()

    def food_repos(self):
        self.goto(find_location())
