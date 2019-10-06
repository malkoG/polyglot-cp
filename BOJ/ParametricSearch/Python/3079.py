def solve(delays, time):
    return sum([time // delay for delay in delays])

N,M=map(int, input().split())
T=[int(input()) for i in range(N)]

lo = 1
hi = 10**18

while lo < hi:
    mid = (lo + hi) // 2
    result = solve(T, mid)

    if result >= M:
        hi = mid
    else:
        lo = mid + 1

print(lo)
