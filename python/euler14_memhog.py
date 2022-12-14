# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def collatz_length(n, memo=None):
    if memo:
        if n in memo.keys():
            return memo[n]
    
    l = 1
    while n != 1:
        if n in memo.keys():
            l += memo[n]
            return l
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        l += 1
    return l

def collatz_length_no_memo(n):
    l = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        l += 1
    return l


@tamd
def find_answer():
    ans = 0
    r_ans = 0
    memo = dict()
    memo[2] = collatz_length(2, dict())
    for x in range(1,1000000):
        l = collatz_length(x, memo)
        memo[x] = l
        if l > ans:
            ans = l
            r_ans = x
            
    return r_ans

    # ans = 0
    # real_ans = 0
    # for x in range(1,10**6):
    #     if (l := collatz_length_no_memo(x)):
    #         if l > ans:
    #             ans = l
    #             real_ans = x
                
    # return real_ans

if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
