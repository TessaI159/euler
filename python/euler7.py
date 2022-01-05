from timer import Timer
from euler import is_prime

def find_answer():
    sieve = prime_sieve(10**4)

# Returns a list of all primes less than n
def prime_sieve(n):
    sieve = [x for x in range(3,n,2)]

    for p in sieve:
        if is_prime(p):
            x = p * 2
            while x < sieve[-1]:
                try:
                    sieve.remove(x)
                except ValueError as e:
                    pass
                x += p
    return sieve

if __name__ == '__main__':
    t = Timer()
    t.time(find_answer)
