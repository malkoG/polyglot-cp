while True:
    try:
        n,k=map(int,input().split())
    except:
        break

    result = []
    for i in range(2, 10**5):
        count = 0
        while k % i == 0:
            k = k // i
            count += 1

        if count > 0:
            result.append((i, count))

    if k > 1:
        result.append((k, 1))

    answer = 1
    for pair in result:
        m,p=pair
        count = 0
        for i in range(1,p+1):
            count += n//(m**i)

        answer *= m**min(count, p)

    print(answer)
