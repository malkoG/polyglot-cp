while True:
    n=int(input())
    if n==-1:
        break

    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    print("Hour {}: {} cow(s) affected".format(n, a))
