'''
Passing Variables
Pawelski
1/29/2023
Python I

Instructions:
Trace the program to determine how it executes and what it
displays. (Hint: You may want to draw it out on a piece of
scrap paper!) Check your work by running the program. You
may even want to run it in debugging mode to see how the
code executes line by line! Finally, let's discuss the
following questions...
1. What is passed when a variable is given as an argument?
2. Which is better, passing specific value or values stored
   in variables?
'''

import turtle


def square(side):
    '''
    Draws a square with a given side length.
    '''
    for i in range(0, 4):
        t.forward(side)
        t.left(90)


t = turtle.Turtle()
length = int(input("Enter a length >> "))
square(length)
