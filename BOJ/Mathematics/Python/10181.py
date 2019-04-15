def get_factors(N):
	result = []
	for i in range(1,N):
		if N % i == 0:
			result.append(i)

	return result

while True:
	N = int(input())
	if N == -1:
		break
	factors = get_factors(N)
	if N == sum(factors):
		print("{} = {}".format(N, " + ".join(map(str, factors))))
	else:
		print("{} is NOT perfect.".format(N))
