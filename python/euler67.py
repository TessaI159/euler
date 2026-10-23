from pathlib import Path

from decorator import time_and_memory_decorator as tamd
from euler import read_input

filename = Path(__file__).stem


@tamd
def find_answer():
    input_data = read_input(filename)
    input_data.reverse()
    input_data = [x.split(" ") for x in input_data]

    for index_r, row in enumerate(input_data):
        for index_n, num in enumerate(row):
            if index_n == len(row) - 1:
                pass
            else:
                input_data[index_r + 1][index_n] = max(
                    int(num), int(row[index_n + 1])
                ) + int(input_data[index_r + 1][index_n])
    return input_data[-1][-1]


if __name__ == "__main__":
    print(filename, ": ", end="")

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
