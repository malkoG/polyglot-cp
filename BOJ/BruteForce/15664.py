def f(A, result, depth, M):
    if depth == M:
        if len(result) == M:
            print(" ".join(map(str,result)))
        return

    for i in range(len(A)):
        A[i][1] -= 1
        result.append(A[i][0])
        if A[i][1] > 0:
            f(A[i:], result, depth + 1, M)
        else:
            f(A[i+1:], result, depth + 1, M)

        result.pop()
        A[i][1] += 1
        f(A[i:], result, depth + 1, M)

n,m=map(int,input().split())
A=list(map(int,input().split()))
S=[ [item, A.count(item)] for item in sorted(set(A)) ]

f(S, [], 0, m)
