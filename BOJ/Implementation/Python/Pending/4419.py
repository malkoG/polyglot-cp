n=int(input())
arr = [""]
for i in range(n):
    arr.append(input())

votes = []
while True:
    try:
        votes.append(list(map(int, input().split())))
    except:
        break

exclude=set()
for i in range(len(votes[0])):
    counter=[ [0,j] for j in range(n+1) ] 
    result =[ vote[i] for vote in votes if vote[i] not in exclude ]
    entire = 0
    for r in result:
        counter[r][0] += 1
        entire += 1
            
    meaningful_result = [ c for c in counter if c[0] > 0]
    meaningful_result.sort()
    print(meaningful_result)
    if meaningful_result[0][0] == meaningful_result[-1][0]:
        break

#    if meaningful_result[-1][0] > entire // 2:
#        meaningful_result = [meaningful_result[-1]]
#        break

    exclude.add(meaningful_result[0][1])

for result in meaningful_result:
    print(arr[result[1]])
