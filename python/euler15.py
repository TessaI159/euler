from timer import Timer

def find_answer(x):
    c = 1
    for i in range(1, x + 1):
        c = c * (x + i) / i
    return int(c)

t = Timer()
t.time(find_answer, 20)
