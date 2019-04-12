import queue as Q

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
area = [0] * 1010101

def bfs(field, component, x, y, max_x, max_y, num_of_components):
    q = Q.Queue()
    
    component[y][x] = num_of_components
    area[num_of_components] += 1
    
    q.put((y, x))
    while not q.empty():
        current_y, current_x = q.get()
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if next_x > 0 and next_x <= max_x and next_y > 0 and next_y <= max_y and component[next_y][next_x] == 0 and field[next_y][next_x] == '0':
                component[next_y][next_x] = num_of_components
                area[num_of_components] += 1

                q.put((next_y, next_x))

N,M=map(int, input().split())

component = [ ([0] * (M+2)) for i in range(N+2) ]
field = ["0" * (M+2)]
for i in range(N):
   field.append("0" + input() + "0")
field.append("0" * (M+2))

number_of_components = 1
for y in range(1, N+1):
    for x in range(1, M+1):
        if component[y][x] == 0 and field[y][x] == "0":
            bfs(field, component, x, y, M, N, number_of_components)
            number_of_components += 1
            
for y in range(1, N+1):
    for x in range(1, M+1):
        if field[y][x] == "0":
            print("0", end="")
        else:
            acc = 1
            set_of_components = set()
            for i in range(4):
                set_of_components.add(component[y + dy[i]][x + dx[i]])
            acc += sum([ area[s] for s in set_of_components ])
            print(str(acc), end="")
    print()
            
