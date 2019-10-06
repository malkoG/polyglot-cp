from decimal import *
getcontext().prec = 100

def sin(x):
    i, s, fact, num, sign = 1, x, 1, x, 1

    for j in range(350):
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return s

A,B,C=map(Decimal,input().split())
lo=Decimal(0)
hi=Decimal(10**5)
eps=Decimal(1e-30)
for i in range(200):
    mid = Decimal((lo + hi) / 2)
    result = A*mid + B*(sin(mid))
    
    if abs(C-result) < eps:
        print(round(mid, 6))
        exit(0)
    
    if C < result:
        hi = mid
    else:
        lo = mid+eps
print(round(mid,6))
