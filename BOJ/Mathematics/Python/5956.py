def solve(x,y):
    if x % 2 == 0 or y % 2 == 0:
        return 0
    return 1 + 4*solve(x//2, y//2)

print(solve(*map(int,input().split())))
