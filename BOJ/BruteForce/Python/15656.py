def search(arr, result, depth, N):
    if(depth == N):
        print(" ".join(map(str, result)))
    else:
        for item in arr:
            result.append(item)
            search(arr, result, depth + 1, N)
            result.pop()

N,M=map(int,input().split())
search(sorted(map(int,input().split())), [], 0, M)
