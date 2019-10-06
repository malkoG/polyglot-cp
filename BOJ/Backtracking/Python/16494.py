def maximum_sum(arr):
    if len(arr) == 0:
        return 0

    ans = -100000
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            ans = max(ans, sum(arr[i:j]))

    return ans

def solve(arr, result, depth, limit):
    if len(arr) == 0:
        return result if depth == limit else -100000
    
    if depth == limit:
        return result

    ans = -100000
    for j in range(1, len(arr)+1):
        ans = max(solve(arr[j:], result + maximum_sum(arr[:j]), depth + 1, limit), ans)
        
    return ans

n,m=map(int,input().split())
arr=list(map(int, input().split()))
acc=0

print(solve(arr, 0, 0, m))
