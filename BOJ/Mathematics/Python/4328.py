while True:
	s=input()
	if s == "0":
		break
		
	b,p,m=s.split()
	b=int(b)
	m=int(m,b)
	p=int(p,b)
	result=p%m
	if result == 0:
		print(0)
	else:
		arr = []
		while result > 0:
			arr.append(str(result % b))
			result = result // b 
		print("".join(reversed(arr)))
