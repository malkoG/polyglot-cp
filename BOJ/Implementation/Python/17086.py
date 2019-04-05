N,M=map(int,input().split())
sharks= []
for i in range(N):
    spaces=input().split()
    for j in range(len(spaces)):
        if spaces[j] == '1':
            sharks.append((i,j))

ans = 0
for i in range(N):
    for j in range(M):
        distance = 9999999999999
        for shark in sharks:
            distance = min(distance, max(abs(i-shark[0]), abs(j-shark[1])))
        
        ans = max(ans, distance)

print(ans)
