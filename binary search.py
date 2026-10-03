
#FTT    =>  return first True
def check(k):
    return True

l,r = 0,n
while l <= r:
    m = (l+r)//2
    if check(m):
        r = m - 1
    else:
        l = m + 1
return l



#TTF    =>  return last True
def check(k):
    return True

l,r = 0,n
while l <= r:
    m = (l+r)//2
    if check(m):
        l = m + 1
    else:
        r = m - 1
return r
