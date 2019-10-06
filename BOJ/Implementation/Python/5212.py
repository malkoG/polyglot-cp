R,C=map(int, input().split())
earth=[list("." * (C+2)), *[list("." + input() + ".") for i in range(R)], list("." * (C+2))]
earth
maxR,minR=0,2*R
maxC,minC=0,2*C

dy=[0,1,0,-1]
dx=[1,0,-1,0]

for y in range(0,len(earth)):
    for x in range(0,len(earth[y])):
        if earth[y][x] == 'X':
            counter = 0
            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]

                if next_y >= 0 and next_y <= R+1 and next_x >= 0 and next_x <= C+1 and earth[next_y][next_x] == '.':
                    counter += 1

            if counter >= 3:
                earth[y][x] = 'O'

for y in range(len(earth)):
    for x in range(len(earth[y])):
        if earth[y][x] == 'X':
            maxR = max(maxR, y)
            minR = min(minR, y)
            
            maxC = max(maxC, x)
            minC = min(minC, x)


for y in range(minR, maxR + 1):
    for x in range(minC, maxC + 1):
        print('X' if earth[y][x] == 'X' else '.', end='')
    print()
