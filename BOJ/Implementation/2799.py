rows,cols=map(int, input().split())
apartment=[input() for i in range(0, rows*5+1)]
window_counts=[0,0,0,0,0]
for row in range(0,rows):
    current_row = 5*row+1
    for col in range(0,cols):
        matches = 0
        current_col = 5*col+1
        for i in range(0, 4):
            if apartment[current_row+i][current_col:current_col+4] == '****':
                matches += 1
        window_counts[matches] += 1

print(' '.join(list(map(str, window_counts))))
