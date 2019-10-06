def gcd(a,b):
    return b if a % b == 0 else gcd(b, a%b)

x,y=map(int, input().split())
print(x+y-gcd(x,y))
