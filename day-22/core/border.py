from turtle import Turtle


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
