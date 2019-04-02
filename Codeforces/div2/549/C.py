import queue as Q

parents = [-1] * (10**5+10)
marked  = [False] * (10**5+10)
visited = [False] * (10**5+10)
unmarked_childs = [0] * (10**5+10)
           
n=int(input())
root=-1
tree = [ [] for i in range(n+1) ]
que = Q.Queue()
for i in range(n):
    parent, c = map(int, input().split())
    if parent == -1:
        root = i + 1
    else:
        parents[i + 1] = parent
        tree[parent].append(i + 1)
        if c == 1:
           marked[i + 1] = True
        else:
           unmarked_childs[parents[i+1]] += 1

result=[]
que.put((root, 1))
order=1
while not que.empty():
    vertex, level = que.get()

    order += 1
    if unmarked_childs[vertex] == 0 and marked[vertex]:
        result.append(vertex)
    
    for next_vertex in sorted(tree[vertex]):
        if not visited[next_vertex]:
            if unmarked_childs[vertex] == 0 and marked[vertex]:
                parents[next_vertex] = parents[vertex]
            
            visited[next_vertex] = True
            que.put((next_vertex, level + 1))

result = list(map(str, result))
if len(result) > 0:
    print(" ".join(result))
else:
    print(-1)
