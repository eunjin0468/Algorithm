import sys
n = int(sys.stdin.readline())
arr_1 = list(map(int, sys.stdin.readline().split()))
arr_1.sort()
m = int(sys.stdin.readline())
arr_2 = list(map(int, sys.stdin.readline().split()))
dic = {}

for num_1 in arr_1:
    if num_1 in dic:
        dic[num_1]+=1
    else:
        dic[num_1] = 1
for num_2 in arr_2:
    if num_2 in dic:
        print(dic[num_2], end = ' ')
    else:
        print(0, end= ' ')