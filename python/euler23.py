# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from pathlib import Path

from decorator import time_and_memory_decorator as tamd

filename = Path(__file__).stem

upper_limit = 28123


@tamd
def find_answer():
    div_sums = [0] * upper_limit
    for i in range(1, upper_limit // 2):
        for j in range(2 * i, upper_limit, i):
            div_sums[j] += i

    abundants = [x for x in range(12, upper_limit - 12) if div_sums[x] > x]
    b = 0
    for a in abundants:
        b |= 1 << a

    s = 0
    limit = upper_limit - 12
    for a in abundants:
        if a > limit:
            break
        s |= b << a

    return sum(x for x in range(1, upper_limit) if not (s & (1 << x)))


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
