from math import ceil, sqrt
n=int(input())
numbers=map(int,input().split())
print(" ".join([ 1 if ceil(sqrt(i)) ** 2 == i else 0 for i in numbers ]))
