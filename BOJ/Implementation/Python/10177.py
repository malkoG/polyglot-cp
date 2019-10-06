n=int(input())
for i in range(n):
    sums = []
    m=int(input())
    board = [ list(map(int, input().split())) for j in range(m) ]

    sums = [*sums, *[sum(board[j]) for j in range(m) ]]
    for j in range(m):
        sums.append(sum([ board[k][j] for k in range(m)]))

    sums.append(sum([ board[j][j] for j in range(m) ]))
    sums.append(sum([ board[j][m-1-j] for j in range(m) ]))

    is_magic_square = all([ i == sums[0] for i in sums ])
    print( "Magic square of size " + str(m) if is_magic_square else "Not a magic square" )
