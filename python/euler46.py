# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1**2
# 15 = 7 + 2×2**2
# 21 = 3 + 2×3**2
# 25 = 7 + 2×3**2
# 27 = 19 + 2×2**2
# 33 = 31 + 2×1**2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# 5777

from math import sqrt
from euler import prime_sieve, is_prime
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def twice_square_check(n):
    return sqrt(n / 2) % 1 == 0

@tamd
def find_answer():
    sieve = prime_sieve(10000)

    check = 1
    running = True
    while running:
        running = False
        check += 2
        for prime in sieve:
            if prime > check:
                break
            if twice_square_check(check - prime):
                running = True
    return check
        
        
    

    

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
