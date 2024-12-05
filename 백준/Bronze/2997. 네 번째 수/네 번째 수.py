arr = list(map(int, input().split()))
arr.sort()
num = min(arr[1]-arr[0], arr[2]-arr[1])
for i in range(len(arr)):
    if arr[i]+num not in arr:
        print(arr[i]+num)
        break