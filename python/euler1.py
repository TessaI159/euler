from timer import Timer

def sum_arith_seq(b, e):
    e -= 1
    se = e // b

    return ((se * (se + 1)) >> 1) * b

def multiples_sum(n):
    return sum_arith_seq(3,n) + sum_arith_seq(5,n) - sum_arith_seq(15,n)

t = Timer()
t.time(multiples_sum, 1000)

