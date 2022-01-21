import math
import sys

class CustomError(Exception):
    pass

def triangular(n):
    """Returns True if n is a triangular number, False elsewise"""
    return ((-1 + math.sqrt(1 + (8 * n))) / 2) % 1 == 0


def square(n):
    """Returns True if n is a square number, False elsewise"""
    return math.sqrt(n) % 1 == 0


def pentagonal(n):
    """Returns True if n is a pentagonal number, False elsewise"""
    return ((1 + math.sqrt(1 + (24 * n))) / 6) % 1 == 0


def hexagonal(n):
    """Returns True if n is a hexagonal number, False elsewise"""
    return ((1 + math.sqrt(1 + (8 * n))) / 4) % 1 == 0


def heptagonal(n):
    """Returns True if n as a heptagonal number, False elsewise"""
    return ((3 + math.sqrt(9 + (40 * n))) / 10) % 1 == 0


def octagonal(n):
    """Returns True if n as a octagonal number, False elsewise"""
    return ((1 + math.sqrt(3 * n + 1)) / 3) % 1 == 0


def triangle_number(n):
    """Returns the nth triangle number"""
    return n * (n + 1) // 2


def square_number(n):
    """Returns the nth square number"""
    return n**2


def pentagon_number(n):
    """Returns the nth pentagon number"""
    return n * (3 * n - 1) // 2


def hexagon_number(n):
    """Returns the nth hexagon number"""
    return n * (2 * n - 1)


def heptagon_number(n):
    """Returns the nth heptagon number"""
    return (n * (5 * n - 3)) // 2


def octagon_number(n):
    """Returns the nth octagon number"""
    return n * (3 * n - 2)


def transpose(a):
    """Transposes a 2 dimensional array

    each sub-array must be the same length as the outer array
    i.e. the array must be square
    [[1,2,3], [4,5,6], [7,8,9]] returns [[1,4,7], [2,5,8], [3,6,9]]

    If there are more columns than rows, it drops the additional columns
    [[1,2,3], [4,5,6]] returns [[1,4], [2,5]]

    If there are more rows than columns, returns an IndexError
    [[1,2], [3,4], [5,6]] returns IndexError
    """
    return [[row[i] for row in a] for i in range(len(a))]


def read_input(input_file_string=None):
    """Really only useful for euler problems.

    Reads the cooresponding input file for the problem, if applicable.
    Needs to be passed the name of the script without the .py extension
    filename represents this name, and is included in each problem's script
    even if no input is needed
    filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'
    """
    if not input_file_string:
        raise CustomError('No filename passed to read_input')
    input_file_string = f'data/{input_file_string}_input.txt'

    with open(input_file_string) as input_file:
        input_data = input_file.readlines()

    return [x.strip() for x in input_data]


def is_permutation(a, b):
    """Returns True if a is a permutation of b, False elsewise"""
    a = list(str(a))
    b = list(str(b))

    a.sort()
    b.sort()

    return a == b


def mult(m):
    """Like the built-in sum, but uses multiplication instead of addition"""
    answer = 1
    for arg in m:
        answer *= int(arg)
    return answer


def phi(num):
    ans = 1

    for x in range(int(math.sqrt(num))):
        if is_prime(x) and num % x == 0:
            ans *= (1 - 1/x)

    return int(ans*num)


def fact(n):
    """Returns the factorial of n. Compatible with floating point numbers"""
    if n == 0:
        return 1

    if n < 0:
        return 0

    a = 1
    while n > 0:
        a *= n
        n -= 1

    if isinstance(n, float):
        a *= math.gamma(n+1)

    return a


def binom_co(n, k):
    """Returns the binomial coefficient of (n/k)"""
    return fact(n)/(fact(k)*fact(n - k))

def permutations(n, k):
    """Returns nPk"""
    return fact(n)/fact(n - k)


def string_sort(s):
    """Takes a string and returns a sorted string. Capital letters come before lowercase letters"""
    if not isinstance(s, str):
        raise CustomError(f'{s} is not a string')
    s = list(s)
    s.sort()
    s = ''.join(s)
    return s


def caseless_string_sort(s):
    """Takes a string and returns a sorted string with all lowercase letters"""

    if not isinstance(s, str):
        raise CustomError(f'{s} is not a string')
    s = list(s)
    s.sort()
    s = ''.join(s)
    return s


def digital_sum(n):
    """Returns the digital sum of n"""
    n = str(n)
    if len(n) == 1:
        return int(n)
    ans = 0
    for c in n:
        ans += int(c)
    return ans


def n_pandigital(n, l=None):
    """Returns True if pandigital, False elsewise

    If l is not passed, it checks for pandigital from 1 through len(n)
    else checks if it is pandigital from 1 through l
    """
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


def to_binary(num):
    """Converts a decinal integer to binary. Raises an error if passed anything other than an int, or an item that is convertable to int"""
    try:
        num = int(num)
    except ValueError as e:
        return e

    return bin(num).replace('0b', '')


def infinite_primes(num=1):
    """Return a generator that will generate infinite primes

    This is very, very slow.
    If an even value is passed as num, it attempts to start generating
    primes at num - 1
    """
    if num % 2 == 0:
        num -= 1

    while True:

        if is_prime(num):
            yield num
        num += 2


def proper_divisors(n):
    """Returns a set with all the proper divisors of n"""
    ans = [1]
    for x in range(2,int(math.sqrt(n) + 1)):
        if n % x == 0:
            ans.append(x)
            ans.append(int(n/x))
    return set(ans)


def is_prime(n):
    """Returns True if prime, False elsewise"""
    if n < 2:
        return False

    if n == 2:
        return True

    elif n % 2 == 0:
        return False

    else:
        for x in range (2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                return False
    return True


def factors(n):
    """Returns an unsorted list of factors of n"""
    ans = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            ans.append(x)
            ans.append(int(n / x))
    return set(ans)


def is_palindrome(x):
    """Returns True if x is a palindrome, False elsewise.

    No error checking, please only pass lists and strings. 'Abcba' is False because of the capital A
    """
    x = str(x)
    t = list(x)
    t.reverse()
    t = ''.join(t)

    return x == t


def sum_of_squares(n):
    """Returns the sum of squares from 1 through n

    If you need the sum of squares from x through n you can use:
    sum_of_squares(n) - sum_of_squares(x-1) where x < n
    """
    return (n * (n + 1) * ((2 * n) + 1)) // 6


def square_of_sums(n):
    """Returns the square of sums from 1 through n

    If you need the square of sums from x through n you can use:
    (sum_of_seq(n) - sum_of_seq(x-1))**2
    """
    return ((n * (n + 1)) / 2) ** 2

def sum_of_seq(n):
    """Sum of integers from 1 througb n

    If you need the sum of x through n you can use:
    sum_of_seq(n) - sum_of_seq(x-1)
    """
    return (n * (n + 1)) // 2


def prime_sieve(n):
    """Returns a list of all primes up to limit n-1"""
    sieve = [True for x in range(n)]

    sieve[0] = False
    sieve[1] = False
    sieve[2] = True


    for i in range(4,n,2):
        sieve[i] = False
    for i in range(3,n,2):
        if not sieve[i]:
            continue
        if is_prime(i):
            x = i * 2
            while x < n:
                sieve[x] = False
                x += i

    sieve = [i for i,p in enumerate(sieve) if p]

    return sieve


def prime_sieve_gen(n):
    """Returns a generator of all primes up to limit n-1

    Works by crafting a list using the prime_sieve function and
    converting it to a generator. Probably useless, but oh well.
    """
    sieve = [True for x in range(n)]

    sieve[0] = False
    sieve[1] = False
    sieve[2] = True


    for i in range(4,n,2):
        sieve[i] = False
    for i in range(3,n,2):
        if is_prime(i):
            x = i * 2
            while x < n:
                sieve[x] = False
                x += i

    real_sieve = (i for i in range(len(sieve)) if sieve[i])
    return real_sieve



def unique(args, length=None):
    """Takes an arbitrary number of lists. Returns True if all items are unique, False elsewise.

    Don't pass in multiple lists, pass in a list of lists. Sorry.
    unique takes the optional length parameter. If passed, all lists must be that length to be considered True
    Otherwise it defaults to the length of the first list in args
    """
    if not length:
        length = len(args[0])

    check_list = []
    for arg in args:
        if len(arg) != length:
            return False
        for elem in arg:
            check_list.append(elem)

    return len(check_list) == len(set(check_list))


def unique_no_length(args):
    """Takes an arbitrary number of lists. Returns True if all items are unique, False elsewise.

    Don't pass in multiple lists, pass in a list of lists. Sorry.
    """

    check_list = []
    for arg in args:
        for elem in arg:
            check_list.append(elem)

    return len(check_list) == len(set(check_list))


def combine(arr):
    """Multiplies each element by itself for each time it repeats. Returns a list

    For example: combine([2,2,3,3]) returns [4,9]
    combine([3,3,3,4,4,5,5,5]) returns [27,16,125]
    """
    elem_dict = {}

    for elem in arr:
        try:
            elem_dict[elem] += 1
        except KeyError as _:
            elem_dict[elem] = 1

    return [key**value for key, value in elem_dict.items()]


def sum_of_fact(n):
    """Returns the sum of the factorial of each digit in a number

    145 = 1! + 4! + 5! = 145
    """
    sums = 0

    for c in str(n):
        sums += fact(int(c))

    return sums == n


def prime_factors(n):
    """Returns the prime factors of a number.

    One caveat to look out for is that if a square, cube, etc.
    is part of the prime factorization it will return a list with
    2, 3, etc. of that number. For example:
    prime_factors(36) return [2,2,3,3] because the prime factorization
    of 36 is [2**2, 3**2]
    The combine function is a good way to check if two numbers have a unique prime factorization.
    combine(prime_factors(644)) returns [4,7,23] instead of [2,2,7,23]
    combine(prime_factors(646)) returns [2,17,19]
    Which allows them to be considered unique when passed to unique
    Check out euler47.py to see prime_factors, unique, and combine used together.
    This is what they were built for.
    """
    answers = []

    if is_prime(n):
        return [n]

    while n % 2 == 0:
        answers.append(2)
        n /= 2

    for i in range(3,int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            answers.append(i)
            n /= i

    if n > 2:
        answers.append(int(n))

    return answers



# Start of data for euler17.py
# ----------------------------

ones_place = \
    {
        0 : '',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'
    }

tens_place = \
    {
        0 : '',
        1 : 'ten',
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety'
    }

hundreds_place = \
    {
        0 : '',
        1 : 'onehundred',
        2 : 'twohundred',
        3 : 'threehundred',
        4 : 'fourhundred',
        5 : 'fivehundred',
        6 : 'sixhundred',
        7 : 'sevenhundred',
        8 : 'eighthundred',
        9 : 'ninehundred'
    }

teens = \
    {
        0 : 'ten',
        1 : 'eleven',
        2 : 'twelve',
        3 : 'thirteen',
        4 : 'fourteen',
        5 : 'fifteen',
        6 : 'sixteen',
        7 : 'seventeen',
        8 : 'eighteen',
        9 : 'nineteen'
    }

# End of data for euler17.py
# ----------------------------
