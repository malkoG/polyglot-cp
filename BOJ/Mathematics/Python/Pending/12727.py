from math import sqrt

def solve(b, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        s=solve(b,p//2)
        return s*s
    return (b*solve(b,p-1))

base=3+sqrt(5)
for i in range(1, int(input())+1):
    print("Case #{}: {:03}".format(i, int(base**int(input()) % 1000)))
