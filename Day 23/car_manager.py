import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.speed('fast')
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - 10)
