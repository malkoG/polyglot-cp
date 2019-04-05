def f(A, result, string_arr, depth, M):
    if depth == M:
        if len(result) == M:
            string_arr.append(" ".join(map(str,result)))
        return

    for i in range(len(A)):
        result.append(A[i][0])
        f(A, result, string_arr, depth + 1, M)
        result.pop()
        f(A, result, string_arr, depth + 1, M)

n,m=map(int,input().split())
A=list(map(int,input().split()))
S=[ [item, A.count(item)] for item in sorted(set(A)) ]

result = []
f(S, [], result, 0, m)

print("\n".join(result))
