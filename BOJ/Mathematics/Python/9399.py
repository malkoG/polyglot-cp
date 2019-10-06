def solve(n):
    for i in range(0,1000):
        limit = (i+1)*(i+2)//2
        if limit > n-1:
            return (i, n-i*(i+1)//2, (n-i*(i+1)//2) - (i+2) )

    return (0,0)

while True:
    n,m=map(int,input().split())
    if n == 0 and m == 0:
        break
    p=solve(n)
    q=solve(m)

    level_diff = abs(p[0]-q[0])
    left_diff = abs(p[1]-q[1])
    upper_left = p[1] if p[0] < q[0] else q[1]
    lower_left = q[1] if p[0] < q[0] else p[1]
    lays_between = upper_left <= lower_left and upper_left + level_diff >= lower_left
    side_diff = upper_left - lower_left if lower_left < upper_left else lower_left - (upper_left + level_diff)
    print( (0 if lays_between else side_diff) + level_diff)
