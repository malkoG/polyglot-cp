def remove_zero(n):
    result = n
    while result % 10 == 0:
        result = result // 10
    return result

def solve(n):
    result = 1
    for i in range(1, n+1):
        result = i * result
        result = remove_zero(result) % 1000000000
    return result

n=int(input())
print("{:05}".format(solve(n) % 100000))

