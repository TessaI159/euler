import inspect
import math
from pathlib import Path
from collections import Counter


def is_triangular(n):
    """Returns True if n is a triangular number, False otherwise"""
    return ((-1 + math.isqrt(1 + (8 * n))) / 2) % 1 == 0


def is_square(n):
    """Returns True if n is a square number, False otherwise"""
    return math.isqrt(n) % 1 == 0


def is_pentagonal(n):
    """Returns True if n is a pentagonal number, False otherwise"""
    return ((1 + math.isqrt(1 + (24 * n))) / 6) % 1 == 0


def is_hexagonal(n):
    """Returns True if n is a hexagonal number, False otherwise"""
    return ((1 + math.isqrt(1 + (8 * n))) / 4) % 1 == 0


def is_heptagonal(n):
    """Returns True if n as a heptagonal number, False otherwise"""
    return ((3 + math.isqrt(9 + (40 * n))) / 10) % 1 == 0


def is_octagonal(n):
    """Returns True if n as a octagonal number, False otherwise"""
    return ((1 + math.isqrt(3 * n + 1)) / 3) % 1 == 0


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


def convert_to_base(to_convert, base):
    """Converts a base 10 number into an array of digits representing the number
    in base"""
    if type(base) is not int or type(to_convert) is not int:
        raise TypeError("Both to_convert and base must be integers")
    if base < 2:
        raise ValueError("Base must be at least two")
    if to_convert == 0:
        return [0]
    if to_convert < 0:
        is_neg = True
        to_convert *= -1
    else:
        is_neg = False

    number_stack = []

    while to_convert > 0:
        to_convert, remainder = divmod(to_convert, base)
        number_stack.append(remainder)

    if is_neg:
        number_stack.append("-")
    number_stack.reverse()
    return number_stack


def transpose(a):
    """Transposes a 2D rectangular matrix."""
    if not a:
        return []
    try:
        return [list(col) for col in zip(*a, strict=True)]
    except ValueError:
        raise ValueError("Matrix must be rectangular")


def read_input(input_file_string=None):
    """Really only useful for euler problems.

    Reads the corresponding input file for the problem, if applicable.
    Automatically determines the datafile to open based on the calling .py script,
    or accepts an explicit filename without the .py extension.
    """
    if not input_file_string:
        for frame in inspect.stack():
            caller = Path(frame.filename)
            if caller.name != "euler.py":
                input_file_string = caller.stem
                break

    if not input_file_string:
        raise CustomError("Could not determine calling script for read_input")

    input_file_string = f"data/{input_file_string}_input.txt"

    with open(input_file_string) as input_file:
        input_data = input_file.readlines()

    return [x.strip() for x in input_data]


def is_permutation(a, b):
    """Returns True if a is a permutation of b, False otherwise. Case sensitive"""
    sa = str(a)
    sb = str(b)
    return len(sa) == len(sb) and sorted(sa) == sorted(sb)


def mult(m):
    """Like the built-in sum, but uses multiplication instead of addition"""
    mi = [int(arg) for arg in m]
    return math.prod(mi)


def fact(n):
    """Returns the factorial of n. Compatible with floating point numbers"""
    if isinstance(n, int):
        if n < 0:
            raise ValueError("n must be non-negative.")
        return math.factorial(n)
    elif isinstance(n, float):
        return math.gamma(n + 1)
    else:
        raise TypeError("n must be an integer or a float.")


def string_sort(s):
    """Takes a string and returns a sorted string. Capital letters come before
    lowercase letters"""
    if not isinstance(s, str):
        raise TypeError("s is not a string.")
    return "".join(sorted(s))


def caseless_string_sort(s):
    """Takes a string and returns a sorted string with all lowercase letters"""

    if not isinstance(s, str):
        raise TypeError("s is not a string.")
    return "".join(sorted(s.lower()))


def digital_sum(n):
    """Returns the digital sum of n"""
    if type(n) is not int:
        raise TypeError("n must be an integer.")
    return sum(int(c) for c in str(abs(n)))


def complete_digital_sum(n):
    if type(n) is not int:
        raise TypeError("n must be an integer")
    n = abs(n)
    while n > 9:
        n = digital_sum(n)
    return n


def n_pandigital(n, l=None):
    """Returns True if pandigital, False otherwise

    If l is not passed, it checks for pandigital from 1 through len(n)
    else checks if it is pandigital from 1 through l
    """
    if isinstance(n, (list, tuple, set)):
        n = "".join(str(x) for x in n)
    else:
        n = str(n)

    l = int(l) if l is not None else len(n)

    return len(n) == l and set(n) == set("123456789"[:l])


def to_binary(num):
    """Converts a decimal integer to a binary string representation"""
    return f"{num:b}"


def _lazy_primes():
    """Return a generator that will generate infinite primes
    If an even value is passed as num, it attempts to start generating
    primes at num - 1
    """
    yield 2
    yield 3

    comps = {}

    primes_feed = _lazy_primes()
    next(primes_feed)
    p = next(primes_feed)
    psq = p * p
    q = 5

    while True:
        if q not in comps:
            if q < psq:
                yield q
            else:
                step = 2 * p
                next_comp = psq + step
                while next_comp in comps:
                    next_comp += step
                comps[next_comp] = step
                p = next(primes_feed)
                psq = p * p
        else:
            step = comps.pop(q)
            next_comp = q + step
            while next_comp in comps:
                next_comp += step
            comps[next_comp] = step
        q += 2


def infinite_primes(start=1):
    """Generates an infinite sequence of primes starting at the first prime >=
    start"""
    for p in _lazy_primes():
        if p >= start:
            yield p


def prime_factorization(n):
    """Returns the prime factors of n with multiplicity"""
    if n < 2:
        return Counter()

    counts = Counter()

    while n % 2 == 0:
        counts[2] += 1
        n //= 2

    d = 3
    while d * d <= n:
        while n % d == 0:
            counts[d] += 1
            n //= d
        d += 2

    if n > 1:
        counts[n] += 1

    return counts


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

    for i in range(3, int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            answers.append(i)
            n /= i

    if n > 2:
        answers.append(int(n))

    return answers


def proper_divisors(n):
    """Returns a set with all the proper divisors of n"""
    if n <= 1:
        return set()

    divisors = {1}
    step = 1 if n % 2 == 0 else 2
    start = 2 if n % 2 == 0 else 3

    for x in range(start, math.isqrt(n) + 1, step):
        if n % x == 0:
            divisors.add(x)
            divisors.add(n // x)

    return divisors


def sum_of_proper_divisors(n):
    """Returns the sum of the proper divisors of n"""

    if n <= 1:
        return 0

    total = 1
    for p, count in prime_factorization(n).items():
        total *= (p ** (count + 1) - 1) // (p - 1)

    return total - n


def sum_of_divisors(n):
    return sum_of_proper_divisors(n) + n


def is_prime(n):
    """Returns True if prime, False otherwise"""
    if n < 2:
        return False

    if n == 2:
        return True

    elif n % 2 == 0:
        return False

    else:
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                return False
    return True


def factors(n):
    """Returns an unsorted list of factors of n"""
    ans = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            ans.append(x)
            ans.append(int(n // x))
    return set(ans)


def is_palindrome(x):
    """Returns True if x is a palindrome, False otherwise."""

    if isinstance(x, (list, tuple)):
        return x == x[::-1]
    s = str(x)
    return s == s[::-1]


def reverse_num(n):
    """Returns the reverse of an integer number"""
    return int(str(n)[::-1])


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
    return ((n * (n + 1)) // 2) ** 2


def sum_of_seq(n):
    """Sum of integers from 1 through n

    If you need the sum of x through n you can use:
    sum_of_seq(n) - sum_of_seq(x-1)
    """
    return (n * (n + 1)) // 2


def prime_sieve(n):
    """Returns a list of all primes up to limit n-1"""
    if n < 3:
        return [2] if n == 3 else []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    sieve[4::2] = [False] * len(range(4, n, 2))

    for i in range(3, math.isqrt(n), 2):
        if sieve[i]:
            sieve[i * i : n : 2 * i] = [False] * len(range(i * i, n, 2 * i))

    return [i for i, is_p in enumerate(sieve) if is_p]


def unique(args, length=None):
    """Takes an arbitrary number of lists. Returns True if all items are unique, False otherwise.

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
    """Takes an arbitrary number of lists. Returns True if all items are unique, False otherwise.

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

    return [k**v for k, v in Counter(sorted(arr)).items()]


_DIGIT_FACTORIALS = tuple(math.factorial(i) for i in range(10))


def is_factorion(n):
    """Returns True if the sum of the factorials of the digits of n is equal to n

    145 = 1! + 4! + 5! = 145
    """

    return sum(_DIGIT_FACTORIALS[int(c)] for c in str(n)) == n


def totient_product(n):
    """Returns the result of Euler's totient function"""

    result = n  # Initialize result as n

    # Iterate through all prime factors of n
    p = 2
    while p * p <= n:
        # Check if p is a prime factor.
        if n % p == 0:
            # If yes, then update n and result
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1

    # If n is prime
    if n > 1:
        result -= result // n
    return int(result)


# Start of data for euler17.py
# ----------------------------

ones_place = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

tens_place = {
    0: "",
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

hundreds_place = {
    0: "",
    1: "onehundred",
    2: "twohundred",
    3: "threehundred",
    4: "fourhundred",
    5: "fivehundred",
    6: "sixhundred",
    7: "sevenhundred",
    8: "eighthundred",
    9: "ninehundred",
}

teens = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen",
}

# End of data for euler17.py
# ----------------------------
