s1,s2=map(int,input().split())
f1=True
f2=True
for i in range(s1):
	a,b=map(int,input().split())
	f1 = f1 and a==b

for i in range(s2):
	a,b=map(int,input().split())
	f2 = f2 and a==b

if f1 and f2:
	print("Accepted")
elif f1 and !f2:
	print("Why Wrong!!!")
else:
	print("Wrong Answer")
