N,M=map(int, input().split())
chapter=[]
for i in range(M):
    d, p = map(int, input().split())
    chapter.append((d,p))

ans = 0
for i in range(2**M):
    cnt = 0
    
    day = 0
    page = 0
    while i > 0:
        if i % 2 == 1:
            day += chapter[cnt][0]
            page += chapter[cnt][1] 
        cnt += 1
        i >>= 1

    if day <= N:
        ans = max(ans, page)

print(ans)
