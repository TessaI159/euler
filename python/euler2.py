from timer import Timer

def fibonacci_sum(max):
    answer = 2
    current = 2
    previous = 1
    answer, current, previous = 0, 0, 1
    while(current < max):
        previous, current = current, current+previous
        if(current % 2 == 0):
            answer += current
    return answer

t = Timer()
t.time(fibonacci_sum, 4000000)
