from math import sqrt, ceil, floor
def gcd(a,b):
    return b if a % b == 0 else gcd(b, a % b)

a,b=map(int,input().split())
ua=ceil(sqrt(a+1))
lb=floor(sqrt(b))
n=lb-ua+1
m=b-a
g=gcd(n,m)
print("{}/{}".format(n//g,m//g))
