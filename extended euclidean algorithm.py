

# return [x,y,r] in
#    ax + by = r
#    where (x,y) are Bezout's coefficient, gcd r
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
