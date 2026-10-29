# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from pathlib import Path

from decorator import time_and_memory_decorator as tamd
from euler import prime_factorization

filename = Path(__file__).stem


def rep_length(n, d):
    pf = prime_factorization(d)
    d //= 2 ** pf.get(2, 0)
    d //= 5 ** pf.get(5, 0)

    if d == 1:
        return 0

    # Calculate Euler's totient phi(d) using the remaining prime factors
    # (If d is prime, this naturally evaluates to d - 1)
    order = d
    for p in pf:
        if p not in (2, 5) and pf[p] > 0:
            order = order // p * (p - 1)

    new_pf = prime_factorization(order)
    for p, exp in new_pf.items():
        for _ in range(exp):
            if pow(10, order // p, d) == 1:
                order //= p
            else:
                break

    return order


@tamd
def find_answer():
    longest = 0
    best_d = 0
    for d in range(999, 1, -1):
        if longest >= d - 1:
            break
        length = rep_length(1, d)
        if length > longest:
            longest = length
            best_d = d
    return best_d


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
