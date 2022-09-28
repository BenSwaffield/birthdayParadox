'''This program calculates the chance of two people in a room having the same
birthday.
'''

# Import required libarys
from array import array
import matplotlib.pyploy as plt
import random

# Set the amount of people in the room
amount_of_people = 23


def generate_rand_array():
    '''This function generate a random array of birthdays for the people in
    the room.
    '''
    # Create an empty array
    x: array[int] = []
    for i in range(amount_of_people):
        x.append(random.randint(1, 365))
    return x


def check_for_duplicates(rand_array):
    amount_duplicates = 0
    for a in range(len(rand_array)):
        for b in range(a, len(rand_array)):
            if rand_array[a] == rand_array[b]:
                amount_duplicates = amount_duplicates + 1
    return amount_duplicates


'''
def create_testing_data():
    ordered_array = []
    for i in range(amount_of_people):
        ordered_array.append(i)
    return ordered_array
'''


def run_iteration():
    y = amount_of_people
    runs = 0
    while y == amount_of_people:
        runs = runs + 1
        y = check_for_duplicates(generate_rand_array())
        #print(y)
    return runs


def calc_mean(array_of_int):
    total = 0
    for i in array_of_int:
        total = i + total
    return total / len(array_of_int)


try:
    array_of_iterations = []
    while True:
        array_of_iterations.append(run_iteration())

except KeyboardInterrupt:
    print("Average runs till duplicate: ", calc_mean(array_of_iterations))
    print("There is a", 100 / calc_mean(array_of_iterations),"% chance in a room of", amount_of_people, "people that two people share a birthday.")
    print("Iterations", len(array_of_iterations))
    