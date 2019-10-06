for i in range(1, 100000):
    paces=float(input())
    if paces == 0:
        break
    print("User", i)
    for i in range(int(input())):
        print("%.5f" % ((float(input())*paces)/100000.0))
