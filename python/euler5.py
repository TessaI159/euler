from timer import Timer

# I need to be able to control what number I start calculating on and which divisors I loop through
# The number I start calculating on should also be my step
# Start on the number output by the previous
# Example: calc(10) == 2520
# So on calc(11) we start with 2520, move a step of 2520, check only the divisor 11


# In this example, if constraint is 11, step should be equal to calc(10)
def calc(constraint, step=None):
    if constraint == 1:
        return 1
    if not step:
        step = constraint
        div = 2
        loop = True
        current = step
    else:
        div = constraint
        loop = False
        current = step

    if loop:
        while True:
            if current % div != 0:
                div = 2
                current += step
            elif current % div == 0 and div == constraint:
                return current
            div += 1
    else:
        while True:
            if current % div != 0:
                current += step
            else:
                return current

def outer_calc(n):
    s = calc(1)
    for x in range(2, n + 1):
        s = calc(x, s)
    return s
            
t = Timer()
t.time(outer_calc, 20)
