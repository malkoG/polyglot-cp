N=int(input())
for i in range(N):
    d, sack, *potatoes = map(int, input().split())
    possible = False
    for bitset in range(2**10):
        weight = 0
        for i in range(10):
            if bitset % 2 == 1:
                weight += potatoes[i]
            bitset >>= 1
        possible = possible or weight == sack
        
    
    print(str(d) + " " + ("YES" if possible else "NO"))
