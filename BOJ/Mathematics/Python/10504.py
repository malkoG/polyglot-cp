for t in range(int(input())):
    N = int(input())
    M = -1
    for k in range(2,20000):
        temp = N-k*(k+1)//2
        if temp % k == 0 and temp >= 0:
            M = temp//k
            break

    if M == -1:
        print("IMPOSSIBLE")
        continue

    result = [ str(M + i) for i in range(1, k+1) ]
    print("{} = {}".format(N, " + ".join(result)))
