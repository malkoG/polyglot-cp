from math import sqrt, ceil
ans=0
def score(d):
    if d in range(0, 11):
        return 10
    elif d in range(11, 31):
        return 9
    elif d in range(31, 51):
        return 8
    elif d in range(51, 71):
        return 7
    elif d in range(71, 91):
        return 6
    elif d in range(91, 111):
        return 5
    elif d in range(111, 131):
        return 4
    elif d in range(131, 151):
        return 3
    elif d in range(151, 171):
        return 2
    elif d in range(171, 191):
        return 1
    else:
        return 0    
for i in range(int(input())):
    x,y=map(int, input().split())
    ans+=score(ceil(sqrt(x**2+y**2)))
print(ans)
