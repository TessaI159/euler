# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.


# It can be seen that n = 6 produces a maximum n/φ(n) for n ≤ 10.

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

from euler import prime_sieve_gen
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

primes = prime_sieve_gen(1500)

@tamd
def find_answer():
    answer = 1
    # Multiply primes until the result of more multiplication
    # would be greater than our limit, in this case 1000000
    for prime in primes:
        if answer * prime > 10:
            break
        print(prime)
        
        answer *= prime

    return answer


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
