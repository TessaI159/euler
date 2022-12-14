# Insert question description here

from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

numbers = [x for x in range(1,100)]
target = 100
solutions = [1] + [0] * target


@tamd
def find_answer():
    for number in numbers:
        for i in range(number, target + 1):
            solutions[i] += solutions[i - number]
    return solutions[-1]


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

