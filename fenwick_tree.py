


        n = len(nums1)
        bit = [0]*(n+1)

        def query(m):
            m += 1
            roll = 0
            while m > 0:
                roll += bit[m]
                m -= m & (-m)
            return roll

        def update(m, delta):
            m += 1
            while m <= n:
                bit[m] += delta
                m += m&(-m)









# 1-indexed array
def brange(m, isQuery=True):
    while 0 < m <= n:
        yield m
        m = (m & (m-1)) if isQuery else (m | (m-1)) + 1
        #m += lsb(m) * (-1 if isQuery else 1)

def query(m):
    return sum(bit[i] for i in brange(m+1))

def update(m, delta):
    for i in brange(m+1, isQuery=False):
        bit[i] += delta

def lsb(i):
    return i&-i
