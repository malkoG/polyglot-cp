n = int(input())
sequences = list(map(int, input().split()))

candidate = 0

for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            for l in range(k + 1, n):
                ri = 1 
                rj = 1 
                rk = 1 
                rl = 1 

                for m in range(i, j):
                    ri *= sequences[m]

                for m in range(j, k):
                    rj *= sequences[m]

                for m in range(k, l):
                    rk *= sequences[m]

                for m in range(l, n):
                    rl *= sequences[m]

                candidate = max(candidate, ri + rj + rk + rl)

print(candidate)
