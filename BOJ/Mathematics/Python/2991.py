a,b,c,d=map(int, input().split())
pmn=map(int, input().split())
n=a+b
m=c+d
for p in pmn:
    ans = 0
    if p % n in range(1,a+1):
        ans+=1
    if p % m in range(1,c+1):
        ans+=1
    print(ans)
