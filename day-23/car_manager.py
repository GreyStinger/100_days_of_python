import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

found_pos_list = []


def find_pos():
    return 296, 26 * round(random.randint(-240, 240) / 26)


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.penup()
        car.color(random.choice(COLORS))
        car.speed('fast')
        car.shapesize(stretch_wid=2, stretch_len=1)
        car.goto(find_pos())
        self.cars.append(car)

    def car_removal(self, car):
        if car.xcor() < -340:
            self.cars.remove(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())
            self.car_removal(car)
