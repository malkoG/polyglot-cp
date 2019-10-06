while True:
    n=int(input())
    if n == -1:
        break
    time = 0
    record = [ list(map(int, input().split())) for i in range(n) ]
    result = 0
    for r in record:
        result += r[0]*(r[1]-time)
        time = r[1]

    print(result, "miles")
