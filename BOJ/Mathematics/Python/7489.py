def remove_zero(n):
    result = n
    while result % 10 == 0:
        result = result // 10
    return result

def solve(n):
    result = 1
    for i in range(1, n+1):
        result = i * result
        result = remove_zero(result) % 10000
    return result

for i in range(int(input())):
    print("{}".format(solve(int(input())) % 10))

