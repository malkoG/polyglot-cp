n,prev,mx=map(int,input().split())
for i in range(n):
    current=int(input())
    if current < prev:
        print("NTV: Dollar dropped by %d Oshloobs" % (prev - current))

    if current > mx:
        print("BBTV: Dollar reached %d Oshloobs, A record!" % current)
        mx = current

    prev = current
