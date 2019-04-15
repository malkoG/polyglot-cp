def factorial(n):
	return n * factorial(n-1) if n > 0 else 1

def rec(p, w):
	return (p % w, p // w)  

def solve(fr, to, w):
	w1,h1=rec(fr-1, w)
	w2,h2=rec(to-1, w)

	return factorial((w2-w1)+(h2-h1))//(factorial(w2-w1)*factorial(h2-h1))

h,w,m=map(int,input().split())
if(m != 0):
	print(solve(1,m,w)*solve(m,w*h,w))
else:
	print(solve(1,w*h,w))
