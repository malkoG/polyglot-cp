import math

def solve(a,p,m):
    if p == 0:
        return 1
    if p % 2 == 0:
        s = solve(a,p//2,m)
        return (s * s) % m
    return (a * solve(a,p-1,m)) % m

def is_prime(p):
    limit = int(math.sqrt(p))
    return all([p % i != 0 for i in range(2,limit)])

while True:
    p,a=map(int,input().split())
    if p == 0 and a == 0:
        break
    print("yes" if (not is_prime(p)) and solve(a,p,p) == a else "no")
