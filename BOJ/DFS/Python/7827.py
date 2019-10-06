graph = [[]]
visited = [False]

def dfs(u):
    count = 0
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            count += 1
            count += dfs(v)
    return count

def solve(V, E):
    count = 0
    for v in range(1, V+1):
        visited = [ False ] * (E + 2)
        result = dfs(v)
        if (result > 0):
            print(result)
        count += result

    print(count)

t=int(input())
for i in range(t):
    v,e=map(int, input().split())
    graph = [ [] for i in range(v+1) ]
    visited = [ False ] * (e + 2)
    for j in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)

    solve(v, e)
