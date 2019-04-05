A,B=map(int, input().split())
for E in range(A+1,100):
    if str(2**E)[0] == str(B):
        print(E)
        break
