a,p1=map(int,input().split())
r,p2=map(int,input().split())

print("Whole pizza" if a*(10**5)//p1 < (r**2)*314159//p2 else "Slice of pizza")
