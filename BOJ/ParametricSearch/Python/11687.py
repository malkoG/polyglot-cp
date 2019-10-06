def calculate(n):
    return sum([ n // (5**i) for i in range(1, 12) ])

def solve(n):
    lo=1
    hi=10**10
    while lo < hi:
        mid = (lo + hi) // 2
        result = calculate(mid)
        if result >= n:
            hi = mid
        else:
            lo = mid + 1

    check = calculate(lo) == n
    return lo if check else -1

print(solve(int(input())))
