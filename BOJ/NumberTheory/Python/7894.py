from math import ceil, log
threshold=10**5
sieve = [True] * (threshold+1)
sieve[0] = False
sieve[1] = False
limit=10**3+2
for i in range(2,limit):
    if not sieve[i]:
        break
    for j in range(i*i, threshold, i):
        sieve[j] = False

primes = [ i for i in range(2, threshold) if sieve[i] ]

for i in range(int(input())):
    k=int(input())
    result=[]
    for p in primes:
        if k < p:
            break

        count = 0
        power = 1
        while True:
            power *= p
            if power > k:
                break
            count += k//power

        if count > 0:
            result.append((p, count))
        
    ans = 0
    for p in result:
        a,m=p
        ans += m*log(a,10)
    
    print(ceil(ans))
