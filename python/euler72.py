# Consider the fraction n/d where n and d are positive integers. If n < d and
# HCF(n, d) = 1, it is called a reduced proper fraction.
#
# How many elements would be contained in the set of reduced proper fractions
# for d <= 1,000,000?

from pathlib import Path
from decorator import time_and_memory_decorator as tamd

filename = Path(__file__).stem


@tamd
def find_answer(max_d=1_000_000):
    # Initialize phi[i] = i
    phi = list(range(max_d + 1))

    # Sieve of Eratosthenes for Euler's Totient
    for p in range(2, max_d + 1):
        if phi[p] == p:  # p is prime!
            # Apply (1 - 1/p) to all multiples of p
            for multiple in range(p, max_d + 1, p):
                phi[multiple] -= phi[multiple] // p

    # Sum phi(d) for all denominators 2 <= d <= max_d
    return sum(phi[2:])


if __name__ == "__main__":
    print(filename, ": ", end="")
    answer, mem, time = find_answer()
    print(answer)
    print(mem)
    print(time)
