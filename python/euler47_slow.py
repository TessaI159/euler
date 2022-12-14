# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from euler import prime_factors, combine, unique
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(length=4):
    first = 3
    distincts = []

    for x in range(first, first+length):
        distincts.append(combine(prime_factors(x)))
    

    while True:
        first += 1
        distincts.pop(0)
        distincts.append(combine(prime_factors(first + (length - 1))))

        if unique(distincts, length):
            return first
        


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
