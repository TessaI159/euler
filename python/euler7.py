# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from decorator import time_and_memory_decorator as tamd
from euler import is_prime
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    index = 1
    i = 3
    while True:
        if is_prime(i):
            index += 1
        if index == 10001:
            return i
        i += 2

if __name__ == '__main__':
    print(filename, ": ", end="")
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
