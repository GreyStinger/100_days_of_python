import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed('fastest')


def main():
    def forward():
        pen.forward(10)

    def backward():
        pen.back(10)

    def left():
        pen.left(10)

    def right():
        pen.right(10)

    def clear():
        pen.pu()
        pen.ht()
        pen.setpos(0, 0)
        pen.seth(0)
        pen.clear()
        pen.pd()
        pen.st()

    screen.listen()
    screen.onkey(key='w', fun=forward)
    screen.onkey(key='s', fun=backward)
    screen.onkey(key='a', fun=left)
    screen.onkey(key='d', fun=right)
    screen.onkey(key='c', fun=clear)


if __name__ == '__main__':
    main()

screen.exitonclick()
