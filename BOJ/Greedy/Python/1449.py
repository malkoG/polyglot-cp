n,m=map(int,input().split())
arr=list(map(int,input().split()))[::-1]
last=10000000
answer=0
for e in arr:
    if last > e:
        last = e
    elif last < e:
        continue

    answer += 1
    last -= m

print(answer)
