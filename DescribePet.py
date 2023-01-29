'''
Describe Pet
Pawelski
1/29/2023
Python I

Instructions:
Trace the program to determine how it executes and what it displays.
Check your work by running the program. You may even want to run it in
debugging mode to see how the code executes line by line! Finally,
let's discuss the following questions...
1. What happens if you provide only one argument?
2. What happens if you provide two arguments?
3. Can you provide no arguments?
4. Modify the function's header so it looks like this...

def describe_pet(animalType="cat", petName):

   The code no longer works! Why?

5. Modify the program by adding another call to the function so it prints...

I have a fish.
My fish's name is Mr. Fishy.

'''


def describe_pet(pet_name, animal_type="cat"):
    '''
    Prints a short message about a pet.
    '''
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")


describe_pet("Smokey")
describe_pet("Choco", "dog")
