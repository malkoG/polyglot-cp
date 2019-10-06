def solve(green_onions, length):
    return sum([ green_onion // length for green_onion in green_onions])

S,C=map(int,input().split())
green_onions=[ int(input()) for i in range(S) ]
lo = 1
hi = 10**10
while lo < hi:
    mid = (lo + hi + 1) // 2
    result = solve(green_onions, mid)

    if C > result:
        hi = mid - 1
    else:
        lo = mid
        
print(sum(green_onions) - hi*C)
