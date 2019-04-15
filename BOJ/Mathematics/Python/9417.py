def gcd(a,b):
	return b if a % b == 0 else gcd(b, a%b)

for t in range(int(input())):
	arr = list(map(int, input().split()))
	ans = 1
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			ans = max(ans, gcd(arr[i], arr[j]))
	print(ans)
