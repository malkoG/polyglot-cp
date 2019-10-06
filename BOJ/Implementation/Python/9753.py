sieve = [True] * (10**6 + 9)
# generate sieve
sieve[1] = False
for i in range(2, 10**3 + 1):
    if not sieve[i]:
        continue

    for j in range(i*i, 10**6 + 1, i):
        sieve[j] = False

primes = []
for i in range(2, 50000):
    if sieve[i]:
        primes.append(i)

print(len(primes))
        
n=int(input())
for i in range(n):
    target = int(input())
    ans = 10000009
    for j in range(len(primes)):
        for k in range(j+1,len(primes)):
            if primes[i] * primes[j] >= target:
                ans = min(ans, primes[i]*primes[j])

    print(ans)
