# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def pythagorean_triplet(a,b,c):
    """Returns true if a, b, and c form a Pythagorean triplet, false elsewise"""
    return a**2 + b**2 == c**2

@tamd
def find_answer():
    for a in range(1,1000):
        for b in range(a+1, 1000):
            c = 1000 - (a + b)
            if pythagorean_triplet(a,b,c):
                return a*b*c

            
if __name__ == '__main__':
    print(filename, ": ", end="")
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
