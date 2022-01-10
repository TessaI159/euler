from decorator import time_and_memory_decorator as tamd
from euler import fact
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

@tamd
def find_answer(n=100):
    return sum([int(x) for x in str(fact(n))])

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
