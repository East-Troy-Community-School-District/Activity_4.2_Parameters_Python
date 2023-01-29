'''
Parameter Rectangle
Pawelski
1/29/2023
Python I

Instructions:
Trace the program to determine how it executes and what it displays.
(Hint: You may want to draw it out on a piece of scrap paper!)
Check your work by running the program. Finally, let's discuss the
following questions...
1. How many parameters does the function have? How many arguments
   will the function require?
2. In what order are the arguments passed to the parameters?
'''

import turtle


def rectangle(length, width):
    '''
    Draws a rectangle with a given length and width.
    '''
    for i in range(0, 2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)


t = turtle.Turtle()
rectangle(100, 200)
rectangle(200, 100)
