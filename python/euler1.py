from decorator import time_and_memory_decorator as tamd

def sum_arith_seq(b, e):
    se = (e-1) // b

    return ((se * (se + 1)) >> 1) * b

@tamd
def find_answer():
    return sum_arith_seq(3,1000) + sum_arith_seq(5,1000) - sum_arith_seq(15,1000)

if __name__ == '__main__':
    print('euler1')

    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)

