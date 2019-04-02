
dp = [[0,0,0] for i in range(10**5 + 10)]

dp[0][0] = 1

n=int(input())

for i in range(1,n+1):
    dp[i][0] = sum([dp[i-1][j] for j in range(3)]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum([dp[n][i] for i in range(3)]))
