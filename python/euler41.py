# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from decorator import time_and_memory_decorator as tamd
from euler import n_pandigital, is_prime
from itertools import permutations
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    for x in range(9,0,-1):
        string = ''.join([str(c) for c in range(1,x + 1)])
        permutions = sorted(int(''.join(chars)) for chars in permutations(string))
        permutions.reverse()
        for p in permutions:
            if is_prime(p):
                return p
        

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
