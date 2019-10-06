n=int(input())
calls = []
for i in range(n):
    p,t=map(int,input().split())
    calls.append((t,-p))

calls.sort()
count = 1
answer = 0
for call in calls:
    _, deadline, profit = map(abs, call)
    if count > deadline:
        continue
    answer += profit
    count += 1

print(answer)
