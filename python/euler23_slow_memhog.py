# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from decorator import time_and_memory_decorator as tamd
from euler import proper_divisors
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

upper_limit = 28123

def abundant_number(n):
    return sum(set(proper_divisors(n))) > n

def abundant_number_sums(abundant_nums):
    lis = []
    for x in range(len(abundant_nums)):
        for y in range(x, len(abundant_nums)):
            if (abundant_nums[x] + abundant_nums[y] <= upper_limit):
                lis.append(abundant_nums[x] + abundant_nums[y])

    return set(sorted(lis))

@tamd
def find_answer():
    abundant_nums = [x for x in range(12, upper_limit - 12) if abundant_number(x)]
    abundant_nums_sums = abundant_number_sums(abundant_nums)
    return sum([x for x in range(1, upper_limit) if x not in abundant_nums_sums])
    

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

