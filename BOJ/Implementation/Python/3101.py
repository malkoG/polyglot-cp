n,m=map(int,input().split())
r,c=0,0
ans=1
for ch in input():
    if ch == 'U':
        r -= 1
    elif ch == 'D':
        r += 1
    elif ch == 'R':
        c += 1
    else:
        c -= 1

    if r+c < n:
        result=(r+c+2)*(r+c+1)//2
        if (r + c) % 2 == 0:
            ans += result - r
        else:
            ans += result - c
    else:
        result=n*(n+1)//2
        remaining=r+c-n
        result+=n*(n-1)//2-(n-remaining-1)*(n-remaining)//2
        if (r + c) % 2 == 0:
            ans += result + (c-remaining)
        else:
            ans += result + (r-remaining)
print(ans)
