n=int(input())
limit = 0
ans=0
for i in range(100000):
    limit += 1 + 2*i*(i+1)
    if limit > n:
        break
    ans = i+1

print(ans)
