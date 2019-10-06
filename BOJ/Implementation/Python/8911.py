n=int(input())

dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]

for i in range(n):
    ans=0
    direction=0

    minY,maxY,minX,maxX=0,0,0,0
    currentY=0
    currentX=0

    command=input()
    for move in command:
        if move == 'F':
            currentY += dy[direction]
            currentX += dx[direction]
        elif move == 'B':
            currentY -= dy[direction]
            currentX -= dx[direction]
        elif move == 'L':
            direction -= 1
            direction += 4
            direction %= 4
        elif move == 'R':
            direction += 1
            direction %= 4

        minY = min(minY, currentY)
        minX = min(minX, currentX)

        maxY = max(maxY, currentY)
        maxX = max(maxX, currentX)

    print((maxX-minX)*(maxY-minY))
