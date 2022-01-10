# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from decorator import time_and_memory_decorator as tamd
from euler import prime_sieve
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    with open('data/primes.txt') as f:
        read = f.readlines()

    primes = [int(x.strip()) for x in read]
    return primes[10**4]


if __name__ == '__main__':
    print(filename, ": ", end="")
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
