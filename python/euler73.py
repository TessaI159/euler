# <p>Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive
# integers. If $n \lt d$ and $\operatorname{HCF}(n, d)=1$, it is called a
# reduced proper fraction.</p>
# <p>If we list the set of reduced proper fractions for $d \le 8$ in ascending
# order of size, we get:
# $$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7,
# \frac 1 3, \mathbf{\frac 3 8, \frac 2 5, \frac 3 7}, \frac 1 2, \frac 4 7,
# \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7, \frac 3 4, \frac 4 5, \frac 5 6,
# \frac 6 7, \frac 7 8$$</p>
# <p>It can be seen that there are $3$ fractions between $\dfrac 1 3$ and
# $\dfrac 1 2$.</p>
# <p>How many fractions lie between $\dfrac 1 3$ and $\dfrac 1 2$ in the sorted
# set of reduced proper fractions for $d \le 12\,000$?</p>

from pathlib import Path
from decorator import time_and_memory_decorator as tamd

filename = Path(__file__).stem

MAX = 12000

# 1. Precompute distinct prime factors for all d <= 12000 (takes ~2 ms)
prime_factors = [[] for _ in range(MAX + 1)]
for p in range(2, MAX + 1):
    if not prime_factors[p]:
        for multiple in range(p, MAX + 1, p):
            prime_factors[multiple].append(p)


def count_coprime(l, u, factors):
    """
    Counts how many integers in [l, u] are coprime to a number
    whose distinct prime factors are given.
    """
    divisors = [(1, 1)]  # tuples of (divisor, sign)
    for p in factors:
        divisors += [(div * p, -sign) for div, sign in divisors]

    # Principle of Inclusion-Exclusion
    return sum(sign * (u // div - (l - 1) // div) for div, sign in divisors)


@tamd
def find_answer():
    total = 0
    for d in range(5, MAX + 1):
        # We need 1/3 < n/d < 1/2 => d/3 < n < d/2
        l = (d // 3) + 1
        u = (d - 1) // 2
        total += count_coprime(l, u, prime_factors[d])
    return total


if __name__ == "__main__":
    print(filename, ": ", end="")
    answer, mem, time = find_answer()
    print(answer)
    print(mem)
    print(time)
