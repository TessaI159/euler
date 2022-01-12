# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
solutions = [1] + [0] * target


@tamd
def find_answer():
    for coin in coins:
        for i in range(coin, target + 1):
            solutions[i] += solutions[i - coin]
    return solutions[-1]


if __name__ == '__main__':
    print(filename)
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
