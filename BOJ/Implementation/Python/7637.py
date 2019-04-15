while True:
	N=int(input())
	if N == 0:
		break

	res = [0] * 2000
	for i in range(N):
		t1,t2=input().split('-')
		h1,m1=map(int, t1.split(':'))
		h2,m2=map(int, t2.split(':'))
	
		mm1 = h1*60 + m1
		mm2 = h2*60 + m2

		for j in range(mm1, mm2):
			res[j] += 1

	print("conflict" if len([i for i in res if i > 1]) > 0 else "no conflict")
	
