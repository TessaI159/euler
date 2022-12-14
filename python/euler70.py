# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


from euler import prime_sieve, is_permutation
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    primes = prime_sieve(5000)
    primes = [x for x in primes if x > 2000]
    
    limit = 10**7
    best_ratio = 100
    best_number = 0

    
    
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            
            n = primes[i] * primes[j]
            
            if n > limit:
                break
            
            phi = (primes[i] - 1) * (primes[j] - 1)
            ratio = n / phi

            
            if ratio < best_ratio and is_permutation(n, phi):
                best_ratio = ratio
                best_number = n
                

    return best_number
            


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
