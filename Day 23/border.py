from turtle import Turtle

PENSIZE = 2


class Border(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.color('blue')
		self.penup()
		self.speed('fast')
		self.pensize(PENSIZE)

	def draw_main(self):
		self.draw_border()

	def draw_border(self):
		x_cords = -296
		y_cords = 256
		for _ in range(2):
			self.goto(x_cords, y_cords)
			self.setheading(90)
			self.pendown()
			self.forward(280)
			self.penup()
			self.forward(32)
			self.pendown()
			self.forward(280)
			self.penup()
			y_cords *= -1

	def draw_goals(self, level):
		# Draw start and finish and draw level
		pass
