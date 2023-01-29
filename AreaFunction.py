'''
Area Function
Pawelski
1/29/2023
Python I

Instructions:
Trace the program to determine how it executes and what it displays.
Check your work by running the program. You may even want to run it
in debugging mode to see how the code executes line by line! Finally,
let's discuss the following questions...
1. This program calculates the area of a shape. Which shape?
2. This program automatically prints the area. Is there any
   downsides to this?
'''


def area(length, width):
    '''
    Calculates and prints the area of a rectangle.
    '''
    area = length * width
    print("Area: " + str(area))


area(2, 3)
area(5, 6)
