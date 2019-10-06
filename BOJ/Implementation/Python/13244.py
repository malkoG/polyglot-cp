T=int(input())
for i in range(T):
    vertices = int(input())
    degrees = [0] * (vertices + 1)
    edges = int(input())
    for j in range(edges):
        u,v=map(int, input().split())
        degrees[u] += 1
        degrees[v] += 1
    print("tree" if all([d > 0 for d in degrees]) and edges == vertices - 1 else "graph")
