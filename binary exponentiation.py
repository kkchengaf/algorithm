
def _pow(b, e):
    res = 1
    while e > 0:
        if e % 2 == 1:
            res = (res * b) % MOD
        e >>= 1
        b = (b**2) % MOD
    return res



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
                for k in range(len(self.a[1])):
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
"""
print(fibonacci(30))
print(fibonacci(32))
print(fibonacci(100))
print(fibonacci(1000))
print(fibonacci(1_000_000))
print(fibonacci(1_000_000_000))

"""
832040
2178309
687995182
517691607
918091266
21
"""
