# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from euler import prime_sieve, is_prime
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    sieve = prime_sieve(10001)

    sieve = [x for x in sieve if x > 1487]

    mod = 3330
    for prime in sieve:
        prime2 = prime + mod
        prime3 = prime2 + mod

        if is_prime(prime2) and is_prime(prime3):
            if sorted(list(str(prime))) == sorted(list(str(prime2))) and sorted(list(str(prime2))) == sorted(list(str(prime3))):
                return f'{prime}{prime2}{prime3}'
                


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
