
def number_of_factor(n):
    cnt = 0
    for i in range(2, 1+int(n**0.5)):
        if n%i==0:
            cnt += 1
            if n//i != i: cnt += 1
    return cnt

def number_of_factor_less_than(n):
    res = 0
    for i in range(1, n+1):
        res += number_of_factor(i)
    return res

v = number_of_factor_less_than(100000)
print(v)