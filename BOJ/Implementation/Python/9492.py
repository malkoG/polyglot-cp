while True:
	N=int(input())
	if N == 0:
		break

	cards = []
	for i in range(N):
		cards.append(input())

	mid = (N+1)//2
	upper = cards[:mid]
	lower = cards[mid:]

	result = []
	for i in range(len(lower)):
		result.append(upper[i])
		result.append(lower[i])
	
	if N % 2 == 1:
		result.append(upper[-1])
	print("\n".join(result))
