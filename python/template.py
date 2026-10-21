# Insert question description here

from decorator import time_and_memory_decorator as tamd
from pathlib import Path

filename = Path(__file__).stem

@tamd
def find_answer():
    pass


if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
