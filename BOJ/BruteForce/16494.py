N,M=map(int,input().split())
arr=list(map(int,input().split()))

ans = -(10**8)
for bitset in range(2**N):
    bitarray = []
    for i in range(N):
        bitarray.append(bitset % 2)
        bitset >>= 1

    number_of_groups = 0
    prev = 0
    for i in bitarray:
        if prev == 0 and i == 1:
            number_of_groups += 1
        prev = i

    acc = 0
    if number_of_groups == M:
        for i in range(N):
            if bitarray[i] == 1:
                acc += arr[i]
        ans = max(acc, ans)
        print(ans)
        
print(ans)
