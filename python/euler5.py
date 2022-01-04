from timer import Timer

def evenly_divisible(n):
    answer = 20
    divisor = 2
    while(True):
        if(answer % divisor != 0):
            divisor = 2
            answer += 20
        elif(answer % divisor == 0 and divisor == n):
            return answer
        divisor += 1


t = Timer()
t.time(evenly_divisible, 20)
