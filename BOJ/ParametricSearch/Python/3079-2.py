from decimal import *
getcontext().prec = 530

epsilon=Decimal(1e-510)
for i in range(int(input())):
    n=Decimal(int(input()))
    lo = Decimal(1)
    hi = Decimal(10**53)
    for j in range(16000):
        mid = (lo + hi) / Decimal(2)
        result = mid*mid*mid
        
        if result > n:
            hi = mid
        else:
            lo = mid + epsilon

    print(("%.12f" % round(hi, 501))[:-2])
