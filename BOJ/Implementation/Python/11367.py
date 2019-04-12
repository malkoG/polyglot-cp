def report(num):
	if num in range(97, 999):
		return "A+"
	elif num in range(90, 97):
		return "A"
	elif num in range(87, 90):
		return "B+"
	elif num in range(80, 87):
		return "B"
	elif num in range(77, 80):
		return "C+"
	elif num in range(70, 77):
		return "C"
	elif num in range(67, 70):
		return "D+"
	elif num in range(60, 67):
		return "D"
	else:
		return "F"

for t in range(int(input())):
	name, score = input().split()
	print("{} {}".format(name, report(int(score))))
