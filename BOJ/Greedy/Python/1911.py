N,L=map(int, input().split())
ponds=[ list(reversed(list(map(int, input().split())))) for i in range(N) ]
last=10**10
answer=0
for p in reversed(sorted(ponds)):
    e, s = p
    if last >= e:
        last = e-1
    count=(last-s+1+L-1)//L
    answer+=count
    last=last-count*L

print(answer)
