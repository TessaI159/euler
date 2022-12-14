# starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

from euler import is_prime
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer():
    side_length = 7
    prime_count = 8
    corner_count = 13
    prime_ratio = prime_count / corner_count

    # Starting from the top-right and moving anticlockwise
    corners = [31, 37, 43, 49]
    increases = [26, 28, 30, 32]
    
    while prime_ratio >= .1:
        
        for index, increase in enumerate(increases):
            corner_count += 1
            corners[index] += increase
            increases[index] += 8
            
            if is_prime(corners[index]):
                prime_count += 1
        prime_ratio = prime_count / corner_count
        side_length += 2
        
    return side_length
    


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
