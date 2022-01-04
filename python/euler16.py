from timer import Timer

def find_answer(p):
    return sum([int(x) for x in str(2 ** p)])
        

t = Timer()
t.time(find_answer, 1000)
