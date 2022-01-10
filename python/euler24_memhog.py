from decorator import time_and_memory_decorator as tamd
from itertools import permutations
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(string='0123456789', ind=10**6):
    permutions = sorted(''.join(chars) for chars in permutations(string))
    return permutions[ind - 1]


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
