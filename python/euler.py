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

    real_input = []
    for x in input_data:
        real_input.append(x.rstrip("\n"))

    # return [x.rstrip('\n') for x in input_data]
    return real_input


def mult(m):
    answer = 1
    for arg in m:
        answer *= int(arg)
    return answer


def fact(n):
    a = 1
    for x in range(n,0,-1):
        a *= x
    return a


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


def sum_of_squares(x, y):
    ret = 0
    for i in range(x, y+1):
        ret += i**2
    return ret


def square_of_sums(x, y):
    ret = 0
    for i in range(x, y+1):
        ret += i
    return (ret**2)


def remove_duplicates(list):
    ret = []
    for i in list:
        if(i not in ret):
            ret.append(i)
    return ret


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


