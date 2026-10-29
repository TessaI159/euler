# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from pathlib import Path

from decorator import time_and_memory_decorator as tamd
from euler import sum_of_proper_divisors

filename = Path(__file__).stem

upper_limit = 28123


def is_abundant_number(n):
    return sum_of_proper_divisors(n) > n


def abundant_number_sums(abundant_nums):
    is_abundant_bools = [False] * upper_limit
    for i, a in enumerate(abundant_nums):
        for b in abundant_nums[i:]:
            s = a + b
            if s >= upper_limit:
                break
            is_abundant_bools[s] = True
    return is_abundant_bools


@tamd
def find_answer():
    abundant_nums = [x for x in range(12, upper_limit - 12) if is_abundant_number(x)]
    abundant_nums_bools = abundant_number_sums(abundant_nums)
    return sum([x for x in range(1, upper_limit) if not abundant_nums_bools[x]])


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
