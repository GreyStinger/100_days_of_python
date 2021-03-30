import turtle
import random

turtle.colormode(255)
turtle.mode('logo')

pen = turtle.Turtle()

COLOURS = [(153, 88, 31), (225, 152, 72), (209, 148, 18), (29, 31, 182), (87, 80, 228), (153, 56, 127), (164, 13, 84), (37, 94, 181), (238, 215, 76), (203, 67, 152), (15, 27, 79), (75, 12, 55), (77, 38, 15), (203, 126, 169), (128, 146, 206), (239, 223, 178), (95, 79, 13), (223, 86, 53), (143, 31, 14), (52, 122, 77), (37, 179, 150), (14, 173, 199), (118, 185, 143), (13, 54, 23), (46, 37, 242), (18, 99, 40), (233, 161, 190), (170, 159, 244), (202, 235, 203), (198, 211, 234)]


def pen_return():
    pen.speed('fast')
    pen.st()
    pen.seth(270)
    pen.fd(225)
    pen.seth(0)
    pen.fd(225)
    pen.seth(90)
    pen.color('white')


def pen_reset():
    pen.speed('fast')
    pen.st()
    pen.pu()
    pen.seth(180)
    pen.fd(50)
    pen.seth(270)
    pen.fd(450)
    pen.seth(90)
    pen.ht()


def pen_run():
    pen.speed('fastest')
    pen.ht()
    for _ in range(9):
        pen.pencolor(random.choice(COLOURS))
        pen.dot(20, random.choice(COLOURS))
        pen.fd(50)
    pen.dot(20, random.choice(COLOURS))


def pen_init():
    pen.speed('fast')
    pen.shape('circle')
    pen.color('red')
    pen.pensize(0)
    pen.pu()
    pen.seth(270)
    pen.fd(225)
    pen.seth(0)
    pen.fd(225)
    pen.seth(90)


def main():
    pen_init()
    for _ in range(9):
        pen_run()
        pen_reset()
    pen_run()
    pen_return()


if __name__ == '__main__':
    main()

screen = turtle.Screen()
screen.screensize(900, 900)
screen.exitonclick()
