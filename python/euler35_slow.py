# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from euler import prime_sieve, is_prime
from decorator import time_and_memory_decorator as tamd
import inspect


filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def circular_prime(number):
    number = list(str(number))
    new_number = []

    for i in range(len(number) - 1):
        for j in range(len(number)):
            if j == 0:
                continue
            new_number.append(number[j])
        new_number.append(number[0])
        if not is_prime(int(''.join(new_number))):
            return False
        number = new_number.copy()
        new_number.clear()

    return True
    
        
    

@tamd
def find_answer():
    num_of_circulars = 0
    sieve = prime_sieve(10**6)

    for i in sieve:
        if circular_prime(i):
            num_of_circulars += 
    return num_of_circulars


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
