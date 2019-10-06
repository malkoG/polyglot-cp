n=int(input())
for i in range(1, 3000):
    if n < (i*(i+1)//2)**2:
        print(i)
        break
