def solve(N):
	if N >= 10:
		return solve(sum([int(ch) for ch in list(str(N))]))
	else:
		return N

while True:
	N=int(input())
	if N == 0:
		break
	print(solve(N))
