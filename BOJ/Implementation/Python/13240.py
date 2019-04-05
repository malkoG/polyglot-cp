n,m=map(int,input().split())
chess='*.' * (n*m)
for i in range(n):
    print(chess[:m] if i % 2 == 1 else chess[:m][::-1])
    chess=chess[m:]
