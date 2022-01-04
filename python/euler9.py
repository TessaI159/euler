from timer import Timer

def pythagorean_triplet(a,b,c):
    return a**2 + b**2 == c**2

def find_answer():
    for a in range(1,1000):
        for b in range(a+1, 1000):
            c = 1000 - (a + b)
            if pythagorean_triplet(a,b,c):
                return a*b*c

t = Timer()
t.time(find_answer)
