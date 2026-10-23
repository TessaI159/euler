# Insert question description here

from pathlib import Path

from decorator import time_and_memory_decorator as tamd

filename = Path(__file__).stem


@tamd
def find_answer():
    pass


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
