from timer import Timer

def fibonacci_sum(max):
    answer, current, previous = 0, 0, 1
    while(current < max):
        previous, current = current, current+previous
        if(current % 2 == 0):
            answer += current
    return answer

t = Timer()
t.time(fibonacci_sum, 4000000)
