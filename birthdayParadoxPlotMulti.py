'''This program calculates the chance of two people in a room having the same
birthday.
'''
# Need to fix iterations phrasing
# Import required libarys
from array import array
import matplotlib.pyplot as plt
import random
import multiprocessing
import time
amount_of_iterations: int = 1000000

def calculate_bday_chance(amount_of_people: int) -> float:

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

    def run_iteration():
        y = amount_of_people
        runs = 0
        while y == amount_of_people:
            runs = runs + 1
            y = check_for_duplicates(generate_rand_array())
        return runs

    def calc_mean(array_of_int):
        total = 0
        for i in array_of_int:
            total = i + total
        return total / len(array_of_int)

    start = time.perf_counter()
    array_of_iterations = []
    #print("COde a")
    for i in range(amount_of_iterations):
        #print("Running iteration")
        array_of_iterations.append(run_iteration())
        #print("Iteration ran")

    #print("Returning calc mean")
    finish = time.perf_counter()
    print(f"Took {finish-start} seconds to calculate for {amount_of_people} in room.")
    return 100 / calc_mean(array_of_iterations)
    
# Lowest range is 2
if __name__ == '__main__':
    pool = multiprocessing.Pool()
    start = time.perf_counter()
    y = pool.map(calculate_bday_chance, range(2,90))
    finish = time.perf_counter()
    print(f"Time to number crunch: {finish-start} seconds.")
    #print("Length of y", len(y))
    x = []
    for i in range(2,len(y)+2):
        x.append(i)
    plt.xlabel('Number of people in room')
    plt.ylabel('Birthday chance %')
    plt.plot(x, y)
    plt.show()




'''
x = []
y = []
processes = []
for i in range(2,100):
    print("Crunching data for", i, "people in a room")
    bday_chance = calculate_bday_chance(i)
    print("Needed an average of", bday_chance, "iterations")
    x.append(i)
    # Append as a percentage
    y.append(100 / bday_chance)
'''

#plt.xlabel('Number of people in room')
#plt.ylabel('Birthday chance %')
#plt.plot(x, y)
#plt.show()