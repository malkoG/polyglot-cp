parents = [ i for i in range(101010) ]
planets = [0] * 101010

def find(u):
    if parents[u] == u:
        return parents[u]
    else:
        parents[u] = find(parents[u])
        return parents[u]

def merge(u, v):
    left,right = sorted([u,v])
    
    left_root = find(left)
    right_root = find(right)

    if left_root == right_root:
        return
    
    planets[left_root] += planets[right_root]
    parents[right_root] = left_root
    
N,M=map(int, input().split())
for i in range(1,N+1):
    planets[i] = int(input())

for i in range(M):
    u, v = map(int, input().split())
    merge(u, v)
    print(planets[find(u)])
