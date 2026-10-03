

def extend_euclid(a, b):
    _r, r = (a, b)
    _x, x = (1, 0)
    _y, y = (0, 1)
    while r:
        q = _r // r
        _r, r = r, _r - q*r
        _x, x = x, _x - q*x
        _y, y = y, _y - q*y

    return [_x, _y, _r]


def chinese_remainder_thm(remainders, mods):
    M = 1
    for m in mods:
        M *= m

    res = 0
    for r,m in zip(remainders, mods):
        _m = M // m
        rpr = extend_euclid(_m, m)[0]
        while rpr < 0:
            rpr += m
        res += r * _m * rpr

        print("factor for {} is {}".format(m, _m * rpr))

    return [res % M, M]

#print(chinese_remainder_thm([2,4,3],[3,5,7]))

def ask(remainders, mods, n):
    res, m = chinese_remainder_thm(remainders, mods)
    print([res, m])
    while res < n:
        yield res
        res += m


"""

for x in ask([0,2,4,6,8],[2,3,5,7,11], 1200):
factor for 2 is 1155
factor for 3 is 1540
factor for 5 is 1386
factor for 7 is 330
factor for 11 is 210
[734, 2310]
"""
for x in ask([0,2,4,6,8],[2,3,5,7,11], 1200):
    print(x)
