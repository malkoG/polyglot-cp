while True:
	s=input()
	if s == "0 W 0":
		break
	source,transaction,amount = s.split()
	source, amount = int(source), int(amount)

	result = source + (amount if transaction == 'D' else -amount)
	if result <= -200:
		print("Not allowed")
	else:
		print(result)
