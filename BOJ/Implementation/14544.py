t=int(input())
for i in range(1,t+1):
    n,m=map(int,input().split())
    votes = dict()
    for j in range(n):
        votes[input()] = 0
        
    for j in range(m):
        who,score,voter = input().split()
        votes[who] += int(score)

    result = 0
    winner = ""
    for k, v in votes.items():
        if result < v:
            winner = k
            result = v

    cnt = 0
    for k, v in votes.items():
        if result == v:
            cnt += 1

    print("VOTE {}: ".format(i),end="")
    if cnt > 1:
        print("THERE IS A DILEMMA")
    else:
        print("THE WINNER IS {} {}".format(winner, result))
        
