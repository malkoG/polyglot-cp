from math import log10

def get_digits(n):
    result = 0
    for i in range(1,n+1):
        result += log10(i)
    return result

lo = 1
hi = 230000
n = log10(int(input()))
epsilon=0.00000000001
ans = 0

while lo < hi:
    mid = (lo + hi) // 2
    digits = get_digits(mid)

    if abs(digits-n) < epsilon:
        ans = mid
    
    if digits < n:
        lo = mid + 1
    else:
        hi = mid

print(ans)
