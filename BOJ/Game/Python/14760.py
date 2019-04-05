cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    if cnt > 0:
        print()
    board = [ input() for i in range(n) ]
    
    rows = [ list(filter(lambda x: x > 0, map(len, row.split(".")))) for row in board  ]
    for row in rows:
        print(" ".join(list(map(str,row))) if len(row) > 0 else "0")

    transposed = [ "".join(row) for row in zip(*board)]
    cols = [ list(filter(lambda x: x > 0, map(len, col.split(".")))) for col in transposed ]
    for i in range(n):
        print(" ".join(list(map(str,cols[i]))) if len(cols[i]) > 0 else "0", end=('' if i == n-1 else '\n'))

    cnt += 1
