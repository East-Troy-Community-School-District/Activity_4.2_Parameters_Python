'''
Parameter Square
Pawelski
1/29/2023
Python I

Instructions:
Together, let's run the program in debugging mode by placing
a break point on line 33. Let's also discuss the following
questions...
1. Identify at least one parameter and one argument.
2. What value is passed to side for the following call?

square(50)

3. What does the parameter change about the function?
4. Based on this example, why are parameters useful?
'''

import turtle


def square(side):
    '''
    Draws a square with a given side length.
    '''
    for i in range(0, 4):
        my_turtle.forward(side)
        my_turtle.left(90)


my_turtle = turtle.Turtle()
square(100)
square(90)
square(80)