arr = [list(map(int, input().split())) for _ in range(9)]
max_num, max_row, max_col =0,0,0
for row in range(9):
    for col in range(9):
        if arr[row][col] > max_num:
            max_num = arr[row][col]
            max_row = row
            max_col = col
print(max_num)
print(max_row+1, max_col+1)