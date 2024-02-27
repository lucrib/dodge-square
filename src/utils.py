from random import randint


def next_color():
    while True:
        yield randcolor()


def randcolor():
    return randgamma(), randgamma(), randgamma()


def randgamma():
    return randint(0, 255)


C = next_color()
