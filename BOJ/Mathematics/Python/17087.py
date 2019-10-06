def gcd(a,b):
    return b if a % b == 0 else gcd(b, a % b)

n,s=map(int,input().split())
arr=sorted([ abs(s-i) for i in map(int,input().split()) ])

ans = arr[-1]
for item in arr:
    ans = gcd(ans, item)
print(ans)
