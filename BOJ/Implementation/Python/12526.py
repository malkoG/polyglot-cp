def who(name):
	if name[-1] == 'y':
		return 'nobody'
	elif name[-1] in 'aeiou':
		return 'a queen'	
	else:
		return 'a king'

		
for i in range(1,int(input())+1):
	s=input()
	print("Case #{}: {} is ruled by {}.".format(i, s, who(s)))
