from turtle import Turtle


class Boarder(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fast')
        self.color('white')
        self.hideturtle()
        self.pensize(2)

    def draw_boarder(self):
        self.goto(-226, 226)
        self.setheading(90)
        self.pendown()
        self.forward(452)
        self.right(90)
        self.forward(452)
        self.right(90)
        self.forward(452)
        self.right(90)
        self.forward(452)
