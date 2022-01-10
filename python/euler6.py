from decorator import time_and_memory_decorator as tamd
from euler import square_of_sums, sum_of_squares

@tamd
def find_answer(n=100):
    return int(square_of_sums(n) - sum_of_squares(n))

if __name__ == '__main__':
    print('euler6')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
    
