while True:
    diff=10000009
    ans = 0
    b,n=map(int, input().split())
    if b==0 and n==0:
        break
    for a in range(1, b+1):
        result = abs(b-a**n)
        if result < diff:
            diff = result
            ans = a
    print(ans)
