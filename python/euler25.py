from decorator import time_and_memory_decorator as tamd


@tamd
def find_solution(*args, **kwargs):
    index = 1
    cur, nex = 1, 1

    while len(str(cur)) < 1000:
        cur, nex = nex, cur + nex
        index += 1

    return index


if __name__ == '__main__':
    find_solution()
