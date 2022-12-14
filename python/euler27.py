# Euler discovered the remarkable quadratic formula:

# n**2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer values
# 0 <= n <= 39 However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n**2 - 79n + 1601 was discovered, which produces 80 primes for the
# consecutive 0 <= n <= 79.
# The product of the coefficients is, -79 * 1601, is -126479

# Considering quadratics of the form:

# n**2 + an + b where |a| < 1000 and |b| <= 1000

# Where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4

# Find the products of the coefficents, a and b, for the quadratic expression that produces the maximum
# number of primes for consecutive values of n, starting with n = 0


from decorator import time_and_memory_decorator as tamd
from euler import is_prime
import inspect


filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def euler_quad_form(n):
    return n**2 + n + 41


def tess_quad_form(n, a, b):
    return n**2  + (a * n) + b


@tamd
def find_answer():
    correct_a, correct_b = 0, 0
    max_primes = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while True:
                if is_prime(tess_quad_form(n, a, b)):
                    n += 1
                else:
                    if n > max_primes:
                        max_primes = n
                        correct_a = a
                        correct_b = b
                    break
    return correct_a * correct_b
    

if __name__ == '__main__':
    print(filename, ': ', end='')
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
