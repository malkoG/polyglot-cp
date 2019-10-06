from math import log
MOD=987654321
def solve(n,p):
    if p == 0:
        return 1

    if p % 2 == 0:
        s = solve(n, p//2)
        return (s*s) % MOD

    return (n*solve(n,p-1)) % MOD

sieve=[True] * 1000001
n=int(input())
sieve[0] = False
sieve[1] = False
for i in range(2, 1001):
    if not sieve[i]:
        continue
    
    for j in range(i*i, 1000001, i):
        sieve[j] = False

answer = 1
primes = [i for i in range(2,10**6 + 1) if sieve[i] ]
for p in primes:
    if p > n:
        break
    answer *= solve(p, int(log(n, p)))
    answer %= MOD

print(answer)
