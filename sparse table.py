

def sparse_table_sum(arr):
    n = len(arr)
    st = [[0]*26 for _ in range(n)]
    for i in range(n):
        st[i][0] = arr[i]

    for j in range(1, 26):
        for i in range(n - (1 << j) + 1):
            st[i][j] = (st[i][j-1] + st[i + (1 << (j - 1))][j-1])

    def RSQ(l, r):
        total = 0
        for j in range(25,-1,-1):
            if r-l+1 >= (1 << j):
                total += st[l][j]
                l += (1 << j)
        return total

    return st






def sparse_table_min(arr):
    n = len(arr)
    st = [[0]*26 for _ in range(n)]
    for i in range(n):
        st[i][0] = arr[i]

    for j in range(1, 26):
        for i in range(n - (1 << j) + 1):
            st[i][j] = min(st[i][j-1], st[i + (1 << (j - 1))][j-1])

    def RMQ(l,r):
        k = 0
        while (1<<(k+1)) <= r-l+1:
            k += 1
        return min(st[l][k], st[r - (1 << k) + 1][k])

    return st





def sparse_table(arr, f):
    n = len(arr)
    st = [[0]*26 for _ in range(n)]
    for i in range(n):
        st[i][0] = f(arr[i])

    for j in range(1, 26):
        for i in range(n - (1 << j) + 1):
            st[i][j] = f(st[i][j-1], st[i + (1 << (j - 1))][j-1])
    return st



def sparse_table_RSQ(arr):
    def mysum(x, y=0): return x + y
    st = sparse_table(arr, mysum)

    def query(l, r):
        total = 0
        for j in range(25,-1,-1):
            if r-l+1 >= (1 << j):
                total += st[l][j]
                l += (1 << j)
        return total
    """
    print(query(4,6)) # 1
    print(query(3,5)) # 2
    print(query(0,6)) # 3
    """
#sparse_table_RSQ([0,1,0,1,0,1,0])

def sparse_table_RMQ(arr):
    def mymin(x, y=float("inf")): return min(x, y)
    st = sparse_table(arr, mymin)

    def query(l,r):
        k = 0
        while (1<<(k+1)) <= r-l+1:
            k += 1
        return min(st[l][k], st[r - (1 << k) + 1][k])

    print(query(4,6)) # 1
    print(query(0,3)) # 3
    print(query(0,2)) # 4


sparse_table_RMQ([7,4,6,3,1,5,8])
