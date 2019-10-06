def solve(x,y):
    flag = (x == y) ^ (((x + y) // 2) % 2 == 0)
    if x == y or x == y + 2:
        return str(x + y) if not flag else str(x + y - 1)
    else:
        return "No Number"
    

for i in range(int(input())):
    x,y=map(int, input().split())
    print(solve(x,y))
