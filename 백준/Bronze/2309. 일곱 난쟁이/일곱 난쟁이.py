import sys
input = sys.stdin.readline

length = [int(input()) for _ in range(9)]
length.sort()

arr = sum(length)
arr_ = []

for i in range(9):
    for j in range(i+1, 9):
        if len(arr_)==2:
            continue
        if arr - length[i] - length[j] == 100:
            arr_.append(length[i])
            arr_.append(length[j])

for i in length:
    if i in arr_:
        continue
    print(i)