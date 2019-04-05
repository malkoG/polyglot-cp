S,N=map(int,input().split())
calories=list(map(int, input().split()))

ans = 0
for i in range(0, 2**N):
    subset = i

    total = 0
    bit_counter = []
    for j in range(N):
        bit_counter.append(subset % 2)
        subset //= 2

    for bit in range(len(bit_counter)):
        if bit_counter[bit] == 1:
            total += calories[bit]

    if total <= S:
        ans = max(ans, total)

print(ans)
