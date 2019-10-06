n=int(input())
dp=[0] + [1] * n
dp2=[0] + [1] * n
arr= [int(input()) for i in range(n)]
arr1=[0] + arr
arr2=[0] + list(reversed(arr))

for i in range(1, n+1):
    for j in range(1, i):
        if dp[i] < dp[j] + 1 and arr1[j] < arr1[i]:
            dp[i] = dp[j] + 1

for i in range(1, n+1):
    for j in range(1, i):
        if dp2[i] < dp2[j] + 1 and arr2[j] < arr2[i]:
            dp2[i] = dp2[j] + 1

print(max(dp[1:]))
print(max(dp2[1:]))
