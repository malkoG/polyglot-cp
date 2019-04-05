def gcd(a,b):
    return b if a % b == 0 else gcd(b, a % b)

a,b,n=map(int, input().split())
print("yes" if n//(a*b//gcd(a,b)) > 0 else "no")
