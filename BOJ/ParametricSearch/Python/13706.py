n=int(input())
lo = 1
hi = 10**500
while lo < hi:
    mid = (lo + hi + 1) // 2
    if mid**2 > n:
        hi = mid - 1
    else:
        lo = mid

    # print(lo, hi, mid)
print(hi)
