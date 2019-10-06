dp  = [ [0] * 1002 for i in range(1002) ]
dp2 = [ [0] * 1002 for i in range(1002) ]

acc  = [ [0] * 1002 for i in range(1002) ]
acc2 = [ [0] * 1002 for i in range(1002) ]

dp[0][0] = 1
for i in range(1001):
    dp2[i][1] = i

for H in range(1, 1001):
    current = 0
    for W in range(1001):
        current += dp[W][H-1]
        dp[W][H] = current
    print

for H in range(2, 1001):
    current = 0
    for W in range(1001):
        current += dp2[W][H-1] + W*dp[W][H]
        dp2[W][H] = current
        

n=int(input())
print(dp2[n][n] + 1)
