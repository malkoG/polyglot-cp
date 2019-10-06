while True:
    M,N=map(int,input().split())
    if M == 0 and N == 0:
        break
    Y = 0
    X = 0

    for L in range(M, N+1):
        candidate = len([i for i in range(1,L+1) if L % i == 0])
        if Y < candidate:
            Y = candidate
            X = L

    print("{} {}".format(X,Y))
