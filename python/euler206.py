# <p>Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,<br> where each “_” is a single digit.</p>

from pathlib import Path

from decorator import time_and_memory_decorator as tamd

from math import isqrt

filename = Path(__file__).stem


@tamd
def find_answer():
    max_target = 1929394959697989990
    starting_index = isqrt(max_target)

    for i in range(starting_index, 0, -1):
        if str((i**2))[::2] == "1234567890":
            return i


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
