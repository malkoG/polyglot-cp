def solve(n, k):
    if n == 6174:
        return k
    else:
        la=sorted(list(str(n)))
        lb=reversed(la)
        b=int(''.join(list(lb)))
        a=int(''.join(la))
        return solve(b-a, k + 1)
    
n=int(input())
for i in range(n):
    print(solve(int(input()),0))
