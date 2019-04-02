def f(A, result, depth, M):
    if depth == M:
        if len(result) == M:
            print(" ".join(map(str,result)))
        return

    for i in range(len(A)):
        result.append(A[i][0])
        f(A[i:], result, depth + 1, M)
        
        result.pop()
        f(A[i+1:], result, depth + 1, M)

n,m=map(int,input().split())
A=list(map(int,input().split()))
S=[ [item, A.count(item)] for item in sorted(set(A)) ]

f(S, [], 0, m)
