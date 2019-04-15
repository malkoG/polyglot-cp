def solve(num):
	result = 0
	for i in range(1, num):
		if num % i == 0:
			result += i

	if result > num:
		return "ABUNDANT"
	elif result == num:
		return "PERFECT"
	else:
		return "DEFICIENT"

print("PERFECTION OUTPUT")
for num in map(int, input().split()):
	if num != 0:
		print("{:5}  {}".format(num, solve(num)))
print("END OF OUTPUT")
