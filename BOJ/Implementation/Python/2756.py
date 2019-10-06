from math import ceil, sqrt
def score(x,y):
    r=ceil(sqrt(x**2+y**2))
    if r <= 3:
        return 100
    elif r > 3 and r <= 6:
        return 80
    elif r > 6 and r <= 9:
        return 60
    elif r > 9 and r <= 12:
        return 40
    elif r > 12 and r <= 15:
        return 20

    return 0

for i in range(int(input())):
    positions=list(map(float, input().split()))
    scoreA = 0
    scoreB = 0
    for j in range(3):
        scoreA += score(positions[2*j], positions[2*j+1])
    for j in range(3):
        scoreB += score(positions[6+2*j], positions[6+2*j+1])
    if scoreA > scoreB:
        result = "PLAYER 1 WINS"
    elif scoreA == scoreB:
        result = "TIE"
    else:
        result = "PLAYER 2 WINS"
        
    print("SCORE: {} to {}, {}.".format(scoreA, scoreB, result))
        
