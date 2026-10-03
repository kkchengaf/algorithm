


def prime_factorization_sqrt_n(n):
    factor = []
    numb = n
    for v in range(2, int(n**0.5)+1):
        while numb % v == 0:
            factor.append(v)
            numb //= v
    if numb > 1: factor.append(numb)
    return factor

"""
print(prime_factorization(18))
print(prime_factorization(2**10*3**5))
print(prime_factorization(17))
"""

#list all primes within [2,n]
def SoE(n):
    isPrime = [True] * (n+1)
    isPrime[0:2] = [False,False]
    for i in range(2,int(n**0.5)+1):
        if isPrime[i] and i**2 <= n:
            for j in range(i**2, n+1, i):
                isPrime[j] = False
    return [i for i in range(n+1) if isPrime[i]]

def prime_factorization_wheel(n):
    factor = []
    numb = n
    for v in SoE(int(n**0.5)):
        while numb % v == 0:
            factor.append(v)
            numb //= v
    if numb > 1: factor.append(numb)
    return factor

print(prime_factorization_wheel(21))

print(prime_factorization_wheel(18))
print(prime_factorization_wheel(2**10*3**5))
