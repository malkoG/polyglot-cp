n=int(input())
for i in range(1,100):
    chk = (i+1)*(2**(i+1)-1)+i
    if chk >= n:
        print(i)
        break
