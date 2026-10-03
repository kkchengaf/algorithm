MOD = 1000000007
def matrix_multiple(a, b):
    m,n = len(a),len(b[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(a[0])):
                res[i][j] = (res[i][j] + a[i][k]*b[k][j]) % MOD
    return res

def matrix_power(a, e):
    m = len(a)
    res = [[0]*m for _ in range(m)]
    for i in range(m):
        res[i][i] = 1
    while e:
        if e & 1:
            res = matrix_multiple(res, a)
        a = matrix_multiple(a, a)
        e >>= 1
    return res








def sum_first_n_fibonacci(n):
    if n <= 2: return n
    T = matrix_power([[0,1,0],[1,1,1],[0,0,1]], n)
    f0 = [[0,1,0]]
    res = matrix_multiple(f0, T)
    return res[0][2]

for i in range(10):
    print(sum_first_n_fibonacci(i))
print()
for i in range(10):
    print(sum_first_n_fibonacci(1_000_000_000 - i))

def fibonacci2(n):
    if n <= 1: return n
    T = matrix_power([[0, 1], [1, 1]], n)
    f0 = [[0,1]]
    res = matrix_multiple(f0, T)
    return res[0][0]





MOD = 1000000007
class Matrix:
    def __init__(self, mat=None, L=1):
        if mat is None:
            self.a = [[0]*L for _ in range(L)]
        else:
            self.a = mat

    @staticmethod
    def I(L):
        i_mat = Matrix(mat=None, L=L)
        for i in range(L):
            i_mat.a[i][i] = 1
        return i_mat

    def T(self):
        res = [[0]*len(self.a) for _ in range(len(self.a[0]))]
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                res[j][i] = self.a[i][j]
        return Matrix(res)

    def element_sum(self):
        res = 0
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                res = (res + self.a[i][j]) % MOD
        return res

    def row_sum(self, row):
        res = 0
        for j in range(len(self.a[0])):
            res = (res + self.a[row][j]) % MOD
        return res

    def __mul__(self, other):
        m,n = len(self.a),len(other.a[0])
        res = Matrix([[0]*n for _ in range(m)])
        for i in range(m):
            for j in range(n):
                for k in range(len(self.a[0])):
                    res.a[i][j] = (res.a[i][j] + self.a[i][k]*other.a[k][j]) % MOD
        return res

def mat_pow(arr_2d, e):
    mat = Matrix(arr_2d)
    res = Matrix.I(L=len(mat.a))
    while e:
        if e & 1:
            res *= mat
        mat = mat*mat
        e >>= 1
    return res


def fibonacci(n):
    if n <= 1: return n
    mat = mat_pow([[0, 1], [1, 1]], n)
    f0 = Matrix([[0, 1]]).T()

    return (mat * f0).row_sum(0) % MOD


"""
for i in range(30):
    print(fibonacci(i))
print(fibonacci(30))
print(fibonacci(32))
print(fibonacci(100))
print(fibonacci(1000))
print(fibonacci(1_000_000))
print(fibonacci(1_000_000_000))
"""

print(fibonacci2(30))
print(fibonacci2(32))
print(fibonacci2(100))
print(fibonacci2(1000))
print(fibonacci2(1_000_000))
print(fibonacci2(1_000_000_000))



"""
832040
2178309
687995182
517691607
918091266
21
"""
