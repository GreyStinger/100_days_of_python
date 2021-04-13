import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard
from border import Border


def stop():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing')
screen.mode('logo')

player = Player()

border = Border()
border.draw_main()

cars = CarManager()

screen.onclick(fun=stop)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
