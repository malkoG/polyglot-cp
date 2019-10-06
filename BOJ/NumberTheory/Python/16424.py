from math import sqrt

threshold = 1010101
sieves = [True] * threshold

sieves[0] = False
sieves[1] = False
for i in range(2, int(sqrt(threshold))):
    if not sieves[i]:
        continue

    for j in range(i*i, threshold, i):
        sieves[j] = False

primes = [ i for i in range(threshold) if sieves[i] ]

n=int(input())
count = 0
while True:
    if n < 3:
        break

    for p in primes:
        if sieves[p] and sieves[n-p]:
            count += 1
            n -= 2*p
            break


print(count)
