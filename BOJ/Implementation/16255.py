import string

def f(n):
    if n == 0:
        return
    else:
        f((n-1)//26 )
        print(string.ascii_uppercase[(n+25) % 26], end="")

n=int(input())
for i in range(n):
    f(int(input()))
    print()
