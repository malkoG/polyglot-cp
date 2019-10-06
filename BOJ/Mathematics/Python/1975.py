def solve(n, b):
    return 0 if n % b != 0 else 1 + solve(n//b, b)

for i in range(int(input())):
    answer=0
    n=int(input())
    for b in range(2, n+1):
        answer += solve(n, b)
    print(answer)
