
#O(nloglogn) time complexity
def SoE(n):
    isPrime = [True] * (n+1)
    isPrime[0:2] = [False,False]
    for i in range(2,int(n**0.5)+1):
        if isPrime[i] and i**2 <= n:
            for j in range(i**2, n+1, i):
                isPrime[j] = False
    return [i for i in range(n+1) if isPrime[i]]

print(SoE(100))
print(SoE(29))

print(len(SoE(100000)))
