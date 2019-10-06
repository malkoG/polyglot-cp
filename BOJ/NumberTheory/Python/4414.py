sieve = [True] * (10**5+1)
sieve[0] = False
sieve[1] = False
for i in range(2,10**3+2):
    if not sieve[i]:
        continue
    for j in range(i*i, 10**5, i):
        sieve[j] = False

primes = [ i for i in range(2, 10**5) if sieve[i] ]

out=[]
while True:
    try:
        n,target=map(int,input().split())
    except:
        break

    print(len(primes))
    result=[]
    k = target
    for p in primes:
        if k < p:
            break
        count = 0
        while k % p == 0:
            k = k // p
            count += 1

        if count > 0:
            result.append((p, count))

    if k > 1:
        result.append((k, 1))
        
    flag = True
    for p in result:
        a,m = p
        count = 0
        power = 1
        while True:
            power *= a 
            if power > n:
                break
            count += n//power
            
        flag = flag and count >= m

    print("{} {} {}!".format(target, "divides" if flag else "does not divide", n))
