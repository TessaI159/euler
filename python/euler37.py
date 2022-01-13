# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from euler import is_prime, infinite_primes
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def trunc_left(num):
    num = str(num)[1:]

    while len(num) > 0:
        if not is_prime(int(num)):
            return False
        num = num[1:]
    return True
                        
def trunc_right(num):
    num = str(num)[:-1]

    while len(num) > 0:
        if not is_prime(int(num)):
            return False
        num = num[:-1]
    return True

@tamd
def find_answer():

    sum_primes = 0
    count = 0
    
    infin_primes = infinite_primes(9)


    while count < 11:
        next_prime = next(infin_primes)
        if trunc_left(next_prime) and trunc_right(next_prime):
            count += 1
            sum_primes += next_prime
            
    return sum_primes

    
        


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
