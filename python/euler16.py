# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer(p=1000):
    return sum([int(x) for x in str(2 ** p)])
        

if __name__ == '__main__':
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
