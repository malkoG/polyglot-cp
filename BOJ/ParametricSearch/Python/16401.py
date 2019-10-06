def solve(cookies, amount):
    return sum([cookie // amount for cookie in cookies])

M,N=map(int, input().split())
cookies=list(map(int, input().split()))

lo = 1
hi = 1000000000
flag = False
while lo < hi:
    mid = (lo + hi + 1) // 2
    result = solve(cookies, mid)

    if result == M:
        flag = True

    if result >= M:
        lo = mid
    else:
        hi = mid - 1

if flag:
    print(lo)
else:
    print(0)
