# This problem description would be ridiculously stupid hard to write here, and I don't care right now.

# Go here instead. https://projecteuler.net/problem=65

# If you're feeling lazy, all you need to know is this:
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536
# The sum of the digits in the numerator of the 10th convergent is 1 + 4 + 5 & 7 = 17

# Find the sum of the digits in the numerator of the 100th convergent of the continued fraction e

from decorator import time_and_memory_decorator as tamd
import inspect
from euler import digital_sum

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

# The numerator is equal to the sum of the previous two numerators
# However, every third numerator is equal to the previous numerator times a_k + the previous numerator before that one
# ^^ This is definitely the most eloquent sentence I've ever written

@tamd
def find_answer():
    index = 3
    k = 1
    prev_numerators = [2, 3]
    numerator_count = 2

    while numerator_count < 100:
        if index % 3 == 0:
            mod = 2 * k
            k += 1
        else:
            mod = 1

        prev_numerators.append(mod * prev_numerators[index - 2] + prev_numerators[index - 3])
        numerator_count += 1
        index += 1

    return digital_sum(prev_numerators[-1])

    


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
