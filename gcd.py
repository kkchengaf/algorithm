
#euclidean algorithm, O(logn) time complexity

def gcd(a, b):
    while b:
        t = a % b
        a,b = b,t
    return a

def lcm(a,b):
    return a//gcd(a,b)*b

print(gcd(60,100))
print(lcm(100,60))
