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

while True:
    n=int(input())
    if n == 0:
        break

    count = 0
    for p in primes:
        if p > n // 2:
            break
        if sieves[p] and sieves[n-p]:
            count += 1

    print(count)
