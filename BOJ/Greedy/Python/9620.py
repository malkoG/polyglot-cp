for i in range(int(input())):
    meetings = []
    while True:
        s,e = map(int, input().split())
        if e == 0 and s == 0:
            break

        meetings.append([e,s])

    meetings.sort()
    current = 0
    answer  = 0
    for meeting in meetings:
        if current <= meeting[1]:
            answer += 1
            current = meeting[0]
        else:
            pass

    print(answer)
