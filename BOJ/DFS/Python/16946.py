dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
area = [0] * 1010101

def dfs(field, component, x, y, max_x, max_y, num_of_components):
    component[y][x] = num_of_components
    area[num_of_components] += 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if next_x > 0 and next_x <= max_x and next_y > 0 and next_y <= max_y and component[next_y][next_x] == 0 and field[next_y][next_x] == '0':
            dfs(field, component, next_x, next_y, max_x, max_y, num_of_components)

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
            dfs(field, component, x, y, M, N, number_of_components)
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
            
