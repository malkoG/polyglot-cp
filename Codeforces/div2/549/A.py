import queue as Q

n=int(input())
arr=list(map(int, input().split()))
counter = [0,0]
for i in range(n):
    counter[arr[i]] += 1
    
for i in range(n):
    counter[arr[i]] -= 1
    if counter[0] == 0 or counter[1] == 0:
        print(i+1)
        break
