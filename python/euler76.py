# It is possible to write 5 as a sum in 6 different ways

# 4+1
# 3+2
# 3+1+1
# 2+2+1
# 2+1+1+1
# 1+1+1+1+1

from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

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

