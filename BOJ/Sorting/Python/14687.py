N=int(input())
arr=sorted(list(map(int,input().split())))
mid = (N+1)//2
small = list(reversed(arr[:mid]))
big = arr[mid:]
ans = []
for i in range(min(len(small),len(big))):
	ans.append(small[i])
	ans.append(big[i])

if N % 2 == 1:
	ans.append(small[-1])

print(" ".join(map(str, ans)))
