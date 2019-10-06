for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(1,n):
        for j in range(i):
            ans += 1 if a[j] <= a[i] else 0
            
    print(ans)
