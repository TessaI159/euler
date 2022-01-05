from timer import Timer
from euler import proper_divisors

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

def find_answer():
    abundant_nums = [x for x in range(12, upper_limit - 12) if abundant_number(x)]
    abundant_nums_sums = abundant_number_sums(abundant_nums)
    return sum([x for x in range(1, upper_limit) if x not in abundant_nums_sums])
    

t = Timer()
t.time(find_answer)

