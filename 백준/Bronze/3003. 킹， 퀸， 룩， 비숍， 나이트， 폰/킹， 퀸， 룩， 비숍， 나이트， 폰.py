arr = list(map(int, input().split()))
list = [1,1,2,2,2,8]
for i in range(len(arr)):
    if list[i] > arr[i]:
        print(list[i]-arr[i], end=' ')
    elif list[i] < arr[i]:
        print(f'-{arr[i]-list[i]}', end=' ')
    elif list[i] == arr[i]:
        print('0', end=' ')