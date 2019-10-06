from math import pi, atan
while True:
    x,y=map(int,input().split())
    if x==0 and y==0:
        break
    if x==0:
        print(90)
    else:
        print(round(atan(abs(y)/abs(x)) / pi * 180))
