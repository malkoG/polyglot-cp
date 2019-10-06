while True:
    n=int(input())
    if n==0:
        break
    printed=[False] * (101010)
    targets=input().split(',')
    for target in targets:
        pages=list(map(int, target.split('-')))
        for i in range(pages[0], pages[-1]+1):
            if i <= n:
                printed[i] = True

    print(printed.count(True))
