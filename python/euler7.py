from timer import Timer
from euler import is_prime

def find_answer():
    x = 2
    prime_index = 0
    while(True):
        if(is_prime(x)):
            prime_index += 1
            if(prime_index == 10001):
                return x
        x += 1

if __name__ == '__main__':
    t = Timer()
    t.time(find_answer)
