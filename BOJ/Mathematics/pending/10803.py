dp = [[11010] * 110 for i in range(10100) ]
visited = [[False] * 110 for i in range(10100) ]

def f(a,b):    
    if a < b:
        return f(b, a)
    else:        
        if visited[a][b] and dp[a][b] > 0:
            return dp[a][b]

        if a % b == 0:
            dp[a][b] = a//b
            visited[a][b] = True
            return dp[a][b]
        
        half = b//2
        for k in range(1, b+1):
            dp[a][b] = min(dp[a][b], (f(a, k) + f(a, b-k) if a % k == 0 else f(b, k) + f(b, a-k) ))

        visited[a][b] = True
        return dp[a][b]

print(f(*map(int,input().split())))
