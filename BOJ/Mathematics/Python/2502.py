result=0
N,K=map(int,input().split())
for b in range(1, 200):
    for a in range(b):
        aa=a
        bb=b
        for i in range(N-2):
            aa,bb=bb,aa+bb
        if bb == K:
            print(a)
            print(b)
            exit(0)
