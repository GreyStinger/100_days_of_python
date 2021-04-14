import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard
from border import Border

game_is_on = True
threader = None

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing')
screen.mode('logo')

player = Player()

border = Border()
border.draw_main()

cars = CarManager()


def stop():
    global game_is_on
    game_is_on = False


def timer():
    time.sleep(1)
    return True


def random_gen():
    if random.randint(0, 2) == 0:
        cars.create_car()


screen.listen()
screen.onkeypress(key='Escape', fun=stop)
screen.onkeypress(key='w', fun=player.player_move)

for _ in range(50):
    random_gen()
    cars.move_cars()


while game_is_on:
    random_gen()
    cars.move_cars()
    time.sleep(0.1)
    screen.update()
    print(cars.cars)
