from decimal import *

for i in range(int(input())):
    n=int(input())
    lo = 1
    hi = 10**51
    for j in range(10000):
        mid = (lo + hi) / 2
        if mid**3 > n:
            hi = mid
        else:
            lo = mid

    print("%.10f" % round(hi-5e-11, 10))
