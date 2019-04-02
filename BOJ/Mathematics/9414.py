T=int(input())
threshold=5*(10**6)
for i in range(T):
    prices = []
    while True:
        N=int(input())
        if N == 0:
            break
        prices.append(N)

    total = 0
    prices = list(reversed(sorted(prices)))
    for i in range(0, len(prices)):
        total += 2 * (prices[i] ** (i+1))

    if total > threshold:
        print("Too expensive")
    else:
        print(total)
