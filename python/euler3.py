# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Answer: 6857

from euler import is_prime, prime_factors
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    return prime_factors(600851475143)[-1]


if __name__ == '__main__':
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
