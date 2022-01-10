from decorator import time_and_memory_decorator as tamd

def pythagorean_triplet(a,b,c):
    return a**2 + b**2 == c**2

@tamd
def find_answer():
    for a in range(1,1000):
        for b in range(a+1, 1000):
            c = 1000 - (a + b)
            if pythagorean_triplet(a,b,c):
                return a*b*c

            
if __name__ == '__main__':
    print('euler9')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
