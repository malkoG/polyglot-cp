def solve(a,b,c):
    if b==0:
        return 1    
    if b%2==0:
        s=solve(a,b//2,c)
        return (s*s)%c
    return (a*solve(a,b-1,c))%c

print(solve(*map(int,input(),split())))