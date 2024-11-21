a,b = map(int, input().split())
arr1, arr2 = [], []
for i in range(a):
    arr1.append(list(map(int, input().split())))
for i in range(a):
    arr2.append(list(map(int, input().split())))
for i in range(a):
    for j in range(b):
        print(arr1[i][j]+arr2[i][j], end=' ')
    print("")
