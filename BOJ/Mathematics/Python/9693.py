N = 1
while(True):
	M = int(input())
	if M == 0:
		break
	ans = 0
	for i in [5 ** d for d in range(1, 11)]:
		ans += M // i
	print("Case #{}: {}".format(N, ans))
	N += 1
