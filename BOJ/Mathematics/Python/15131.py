n=int(input())
if n % 3 == 0:
    print((n//3)*7)
elif n % 3 == 1:
    print((n//3-1)*7+4)
elif n % 3 == 2:
    print((n//3)*7+1)
