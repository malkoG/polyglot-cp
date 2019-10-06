n,m=map(int,input().split())
ans = 0
board = [list(map(int, input().split())) for i in range(n)]
board = [[0] * (m+2)] + [[0, *line, 0] for line in board ]  + [[0] * (m+2)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(1, n+1):
    for j in range(1, m+1):
        for k in range(4):
            nx=j+dx[k]
            ny=i+dy[k]
            ans += max(0, board[i][j]-board[ny][nx]) 
    
ans += 2*n*m

print(ans)
