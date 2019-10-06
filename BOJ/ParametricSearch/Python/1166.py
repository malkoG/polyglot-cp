def solve(a,l,w,h):
    return int(l/a)*int(w/a)*int(h/a)

N,L,W,H=map(int,input().split())

lo = 1
hi = 10**100
epsilon=0.000000001
ans = -1
while hi-lo > epsilon:
    mid = (lo + hi) / 2
    
    result=solve(mid, L, W, H) 

    if result < N:
        hi = mid
    else:
        lo = mid + epsilon

print("%0.13f" % abs(mid))
