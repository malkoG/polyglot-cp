def solve(n,b):
    if n == 0:
        return 0
    r=n%b
    return r ** 2 + solve(n//b, b)

for i in range(int(input())):
    p,b,n=map(int,input().split())
    print(p, solve(n,b))
