# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the 

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from decorator import time_and_memory_decorator as tamd
from itertools import permutations
from euler import is_prime
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    permutions = sorted(''.join(chars) for chars in permutations('0123456789') if ''.join(chars)[0] != '0')
    primes = [x for x in range(18) if is_prime(x)]

    total = 0
    for p in permutions:
        thorough = True
        for prime, sub in zip(primes, range(1,8)):
            if not int(p[sub:sub+3]) % prime == 0:
                thorough = False
        if thorough:
            total += int(p)
    return total
            

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
