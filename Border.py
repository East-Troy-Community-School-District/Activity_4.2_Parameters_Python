'''
Border
Pawelski
1/29/2023
Python I

Instructions:
Read through the code so you understand how the program works.
Currently, the function displays a border consisting of tildas
(HINT: a tilda looks like this "~") that is 50 long. Modify the
method so that it accepts a symbol and length as parameters. Using
these parameters, the function should draw a border. While updating
your function, don't forget to update the docstring. In addition to
modifying the function, update the call to the function so that it
displays a border consisting of "*" that is 100 long.
'''

def print_border():
    '''
    Prints a border consisting of "~" that is 50 long.
    '''
    for i in range(0, 50):
        print("~", end="")
    print()


print_border()