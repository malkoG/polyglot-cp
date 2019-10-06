T=[3,2,1]
A=[int(input()) for i in range(3)]
B=[int(input()) for i in range(3)]
resultA=0
resultB=0
for i in range(3):
    resultA += A[i]*T[i]
    resultB += B[i]*T[i]
if resultA > resultB:
    print("A")
elif resultA == resultB:
    print("T")
else:
    print("B")
