from decorator import  time_and_memory_decorator as tamd

@tamd
def find_answer():
    answer, current, previous = 0, 0, 1
    while(current < 4000000):
        previous, current = current, current+previous
        if(current % 2 == 0):
            answer += current
    return answer


if __name__ == '__main__':
    print('euler2')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
