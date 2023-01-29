'''
Polygon
Pawelski
1/29/2023
Python I

Instructions:
Read through the code so you understand how the program works.
Currently, the program is missing a call to the function polygon().
Add a call so that the program draws a pentagon (5 sides) with
each side being 25 pixels long.
'''

import turtle


def polygon(sides, length):
    '''
    Draws a regular polygon with the given number of sides and
    side lengths.
    '''
    angle = 180 - (180 * (sides - 2) / sides)
    for i in range(0, sides):
        t.forward(length)
        t.left(angle)


t = turtle.Turtle()
# Add your call here!
