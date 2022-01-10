from decorator import time_and_memory_decorator as tamd
from euler import prime_sieve

@tamd
def find_answer():
    with open('data/primes.txt') as f:
        read = f.readlines()

    primes = [int(x.strip()) for x in read]
    return primes[10**4]


if __name__ == '__main__':
    print('euler7')
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
