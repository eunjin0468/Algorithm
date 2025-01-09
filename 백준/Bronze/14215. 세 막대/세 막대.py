arr = sorted(map(int, input().split()))
if arr[0]+arr[1] > arr[2]:
    print(sum(arr))
else:
    print((arr[0]+arr[1])*2-1)