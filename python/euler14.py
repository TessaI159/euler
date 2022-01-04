from timer import Timer

def collatz_length(n, memo):
    if n in memo.keys():
        return memo[n]
    
    l = 1
    while n != 1:
        if n in memo.keys():
            l += memo[n]
            return l
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        l += 1
    return l



def find_answer():
    ans = 0
    r_ans = 0
    memo = dict()
    memo[2] = collatz_length(2, dict())
    for x in range(1,1000000):
        l = collatz_length(x, memo)
        memo[x] = l
        if l > ans:
            ans = l
            r_ans = x
            
    return r_ans

t = Timer()
t.time(find_answer)
