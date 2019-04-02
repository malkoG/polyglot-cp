dp = [0 for i in range(10**6+10)]

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 10**6+10):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % (10**9+9)

n=int(input())
for i in range(n):
    print(dp[int(input())])
