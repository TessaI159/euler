# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from euler import prime_sieve, is_prime
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'



@tamd
def find_answer(limit=10**6):
    # Starting at 2, how many primes does it take to add to limit?
    primes = []
    with open('data/primes.txt') as fptr:
        lines = fptr.readlines()

    for line in lines:
        primes.append(int(line.strip()))

    primes_below_limit = [x for x in primes if x < limit]
    
    

    psum = 0
    term_limit = 0
    while psum < limit:
        psum += primes[term_limit]
        term_limit += 1

    for loop_limit in range(term_limit, 0, -1):
        for x in range(len(primes_below_limit) - loop_limit):
            greatest_sum = sum(primes_below_limit[x:x+loop_limit])
            if greatest_sum  >= limit:
                break
            if is_prime(greatest_sum):
                return greatest_sum
    
        
    
            
    

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
