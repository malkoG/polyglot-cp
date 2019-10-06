from bisect import bisect_left, bisect_right

N=int(input())
result = set()
is_good = [False] * 2002

A=list(sorted(map(int, input().split())))
for j in range(len(A)):
    for i in range(j):
        target=A[i]+A[j]
        if j+1 != len(A):
            left =bisect_left(A, target, j + 1, len(A))
            right=bisect_right(A, target, j + 1, len(A))
            if left != len(A) and A[left] == target:
                for k in range(left,right):
                    if is_good[k]:
                        break
                    is_good[k] = True
        
        if j - i > 1:
            left =bisect_left(A, target, i + 1, j)
            right=bisect_right(A, target, i + 1, j)
            if left != j and A[left] == target:
                for k in range(left,right):
                    if is_good[k]:
                        break
                    is_good[k] = True

        if i > 0:
            left =bisect_left(A, target, 0, i)
            right=bisect_right(A, target, 0, i)
            if left != i and A[left] == target:
                for k in range(left,right):
                    if is_good[k]:
                        break
                    is_good[k] = True

print(is_good.count(True))
