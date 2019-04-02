while True:
    n=int(input())
    if n == 0:
        break
    print(sorted([input() for i in range(n)], key=str.lower)[0])
