# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, data/euler79_input.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

# I legitimately solved this one by hand before I solved it with Python

from euler import read_input
from decorator import time_and_memory_decorator as tamd
import inspect
from itertools import permutations

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

def in_order(a, b, lis):
    for i, l in enumerate(lis):
        if a == l:
            a_ind = i
        elif b == l:
            b_ind = i

    return a_ind < b_ind
        

def swap(a, b, lis):
    i, j = lis.index(a), lis.index(b)
    lis[i], lis[j] = lis[j], lis[i]


@tamd
def find_answer():
    input_data = read_input(filename)

    passcode = []
    for inp in input_data:
        for num in inp:
            if num not in passcode:
                passcode.append(num)

    for inp in input_data:
        for p in range(2):
            if in_order(inp[p], inp[p + 1], passcode):
                continue
            else:
                swap(inp[p], inp[p + 1], passcode)
    return ''.join(passcode)

    

if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
