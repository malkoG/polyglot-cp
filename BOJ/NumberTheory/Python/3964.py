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
    n,k=map(int,input().split())
    result=[]
    for p in primes:
        count = 0
        while k % p == 0:
            k = k // p
            count += 1

        if count > 0:
            result.append((p, count))
        
    if k > 1:
        result.append((k, 1))

    ans = 9876543219984
    for p in result:
        a,m = p
        count = 0
        power = 1
        while True:
            power *= a
            if power > n:
                break
            count += n//power
            
        ans = min(ans, count//m)

    print(ans)
