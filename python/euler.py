import math
import sys


def transpose(a):
    return [[row[i] for row in a] for i in range(len(a))]


def get_input_string():
    return "data/" + sys.argv[0].rstrip(".py") + "_input.txt"
    

def read_input():
    input_file_string = get_input_string()
    with open(input_file_string) as input_file:
        input_data = input_file.readlines()

    return [x.strip() for x in input_data]


def mult(m):
    if True in [isinstance(m, bool), isinstance(m, dict)]:
        return 0
    if True in  [isinstance(m, int), isinstance(m, float)]:
        return m
        
    answer = 1
    for arg in m:
        answer *= int(arg)
    return answer


def fact(n):
    if True in [isinstance(n, list), isinstance(n, tuple), isinstance(n, bool), \
                isinstance(n, set), isinstance(n, dict)]:
        return 0
    
    if isinstance(n, str) and '.' in n:
        try:
            n = float(n)
        except ValueError as _:
            return 0
        
    elif isinstance(n, str) and '.' not in n:
        try:
            n = int(n)
        except ValueError as _:
            return 0
        
    if n <= 0:
        return 0
    
    a = 1
    while n > 0:
        a *= n
        n -= 1
        
    if isinstance(n, float):
        a *= math.gamma(n+1)
        
    return a

def string_sort(s):
    if not isinstance(s, str):
        return 0
    s = list(s)
    s.sort()
    s = ''.join(s)
    return s


def n_pandigital(n, l=None):
    if True not in [isinstance(n, int), isinstance(n, str), \
                    isinstance(l, int), isinstance(l, float)]:
        return False
    
    if True in [isinstance(n, set), isinstance(n, tuple), isinstance(n, list)]:
        n = [str(x) for x in n]
        n = ''.join(n)
    
    if isinstance(l, float):
        l = int(l)
        
    n = str(n)
    if not l:
        l = len(n)

    if len(n) != l:
        return False

    comp = ''.join([str(x) for x in range(1,l+1)])
    n = string_sort(n)
    comp = string_sort(comp)

    return n == comp



def proper_divisors(n):
    ans = [1]
    for x in range(2,int(math.sqrt(n) + 1)):
        if n % x == 0:
            ans.append(x)
            ans.append(int(n/x))
    return ans
    

def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    elif n % 2 == 0:
        return False
    
    else:
        for x in range (2, int(math.sqrt(n)) + 1):
            if(n % x == 0):
                return False
    return True


def factors(n):
    ans = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            ans.append(x)
            ans.append(int(n / x))
    return set(ans)


def is_palindrome(x):
    x = str(x)
    t = list(x)
    t.reverse()
    t = ''.join(t)

    return x == t


def sum_of_squares(n):
    return (n * (n + 1) * ((2 * n) + 1)) / 6


def square_of_sums(n):
    return ((n * (n + 1)) / 2) ** 2


def remove_duplicates(list):
    ret = []
    for i in list:
        if(i not in ret):
            ret.append(i)
    return ret


def prime_sieve(n):
    sieve = [x for x in range(3,n,2)]

    for p in sieve:
        if is_prime(p):
            x = p * 2
            while x < sieve[-1]:
                try:
                    sieve.remove(x)
                except ValueError as e:
                    pass
                x += p
                
    return sieve


def prime_factors(n):
    original = n
    answer = []
    if is_prime(n):
        return n
    
    for x in range(int(math.sqrt(n)), 1, -1):
        if is_prime(x) and n % x == 0:
            answer.append(x)
            n /= x
    test = 1
    for i in answer:
        test *= i
    if test != original:
        answer.append(int(original / test))
    answer.sort()
    if answer[0] == 1:
        del(answer[0])
    return answer


