from math import sqrt, ceil

def sigma(n):
    return n*(n+1)//2

def solve(n,m):
    x=sqrt((sigma(n) + sigma(m-1)))
    return (ceil(x) == int(x), int(x))

m=int(input())
for n in range(m+2, 10**7):
    possible, x = solve(n, m)
    if possible:
        print(m,x,n)
        break
    
