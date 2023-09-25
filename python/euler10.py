# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Answer is 142913828922

from decorator import time_and_memory_decorator as tamd
from euler import is_prime
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(r=(10**6)*2):
    # This solution works. ~.3 seconds, .03Mb memory
    total = 0
    with open ('data/primes.txt') as file_stream:
        while line := file_stream.readline():
            if int(line) < 2*10**6:
                total += int(line)
            else:
                break
    return total
    
    # This solution takes too long
    # return sum([x for x in range(3,r,2) if is_prime(x)]) + 2

if __name__ == '__main__':
    print(filename, ": ", end="")
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
