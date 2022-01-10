# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101. (1, 3, 5, 7, 9, 13, 17, 21, 25)

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def form_spiral(w, h):
    limit = w * h
    step = 2
    count = 0
    s = 0
    i = 1
    
    while i < limit + 1:
        s += i
        count += 1
        i += step

        if count % 4 == 0:
            step += 2
            count = 4

    return s

        
    
        

@tamd
def find_answer():
    return form_spiral(1001, 1001)


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
