'''
ParameterDebug
Pawelski
1/29/2023
Python I

Instructions:
Try running the program. Currently, it produces an error.
Read through the code to determine how the program works
and correct any errors! When finished, it should draw 100
randomly placed, randomly sized, and randomly colored dots.
'''

import random, turtle


def draw_dot(x, y, size, red, green, blue):
    '''
    Draws a dot with at (x, y) with the given size and color.
    '''
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(red, green, blue)
    t.dot(size)


def draw_dots(number):
    '''
    Draws the indicated number of randomly placed, randomly sized,
    and randomly colored dots.
    '''
    for i in range(0, number):
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        size = random.randint(10, 100)
        r = random.random()
        g = random.random()
        b = random.random()
        draw_dot(x, y, size)


t = turtle.Turtle()
t.speed(0)
draw_dots()
