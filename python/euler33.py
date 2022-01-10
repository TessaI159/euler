from timer import Timer

def simplify_fraction(numerator, denominator):
    divided = True
    while divided:
        divided = False
        for i in range(2,numerator):
            if numerator % i == 0 and denominator % i == 0:
                numerator /= i
                numerator = int(numerator)
                denominator /= i
                denominator = int(denominator)
                divided = True
                
                if denominator % numerator == 0:
                    denominator /= numerator
                    numerator /= numerator
                    numerator = int(numerator)
                    denominator = int(denominator)
    
    return numerator, denominator

def naive_simplify_fraction(numerator, denominator):
    numerator_l = list(str(numerator))
    denominator_l = list(str(denominator))

    if '0' in numerator_l and '0' in denominator_l:
        return 0, 0

    if numerator_l[0] in denominator_l:
        denominator_l.remove(numerator_l[0])
        numerator_l.remove(numerator_l[0])
        return int(''.join(numerator_l)), int(''.join(denominator_l))
        
    elif numerator_l[1] in denominator_l:
        denominator_l.remove(numerator_l[1])
        numerator_l.remove(numerator_l[1])
        return int(''.join(numerator_l)), int(''.join(denominator_l))

    return 0, 0
        


def find_solution():
    frac = []
    naive = []
    simp = []
    dumb_frac = []
    for a in range(10,100):
        for b in range(a+1,99):
            naive.append(naive_simplify_fraction(a,b))
            simp.append(simplify_fraction(a,b))
            frac.append((a, b))

    for n, s, f in zip(naive, simp, frac):
        if 0 not in n:
            if int(n[0]) / int(n[1]) == int(s[0]) / int(s[1]):
                dumb_frac.append(f)
    a_total = 1
    b_total = 1
    
    for a, b in dumb_frac:
        a_total *= a
        b_total *= b

    return simplify_fraction(a_total, b_total)[1]
                
    
t = Timer()
t.time(find_solution)
