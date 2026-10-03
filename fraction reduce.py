
def gcd(a, b):
    while b:
        t = a % b
        a,b = b,t
    return a

def frac_reduce(a, b):
    g = gcd(a, b)
    print("gcd of {} and {} is {}".format(a,b,g))
    return [a//g, b//g]


print(frac_reduce(12345,99999))
print(frac_reduce(142857142857,999999))
