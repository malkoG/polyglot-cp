digit="0123456789"
count=[0] * 10
n,m=map(int, input().split())
for i in range(n, m+1):
    s=str(i)
    for j in range(10):
        count[j] += s.count(digit[j])

print(" ".join(map(str,count)))
