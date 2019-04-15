for i in range(int(input())):
	a,b=map(lambda x: x[::-1],input().split())
	print(int(str(int(a)+int(b))[::-1]))
