from decorator import time_and_memory_decorator as tamd
from euler import is_prime

@tamd
def find_answer(r=(10**6)*2):
    return sum([x for x in range(3,r,2) if is_prime(x)]) + 2

if __name__ == '__main__':
    print('euler10')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
