dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
for i in range(1,int(input())+1):
    board = [ [0] * 70 for i in range(70) ]
    
    x,y=map(int,input().split())
    board[y][x] = 1
    direction=0
    
    for ch in input():
        if ch == 'F':
            x += dx[direction]
            y += dy[direction]
            board[y][x] += 1
        elif ch == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4

    n=0
    for xx in range(65):
        for yy in range(65):
            n += 1 if board[yy][xx] > 1 else 0
    
    print("Case #{}: {} {} {}".format(i, x, y, n))
