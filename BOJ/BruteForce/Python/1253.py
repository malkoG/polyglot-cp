n=int(input())
strings=input().split()
numbers=list(map(int, strings))
h=dict()
counter=dict()
for s in strings:
    h[s] = 0
    try:
        counter[s] += 1
    except:
        counter[s] = 1

for i in range(n):
    for j in range(i+1, n):
        try:
            result = numbers[i] + numbers[j]
            h[str(result)] += 1
        except:
            pass

ans = 0
print(set(strings))
for s in set(strings):
    if h[s] > 0:
        ans += counter[s]

print(ans)
