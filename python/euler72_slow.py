# Consider the fraction n/d where n and d are positive integers. If n<d and
# GCD(n,d)=1 this is called a reduced proper fraction.

# How many reduced proper fractions are there for d\le 10^6?

from euler import euler_totient_product
from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer():
    r=0
    for d in range(2,10**6+1):
       r += euler_totient_product(d)
    return r

if __name__ == '__main__':
    print(filename, ': ', end='')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

