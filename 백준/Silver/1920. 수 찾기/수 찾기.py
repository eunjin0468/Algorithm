n = int(input())
arr_1 = list(map(int, input().split()))
arr_1.sort()
m = int(input())
arr_2 = list(map(int, input().split()))

for num in arr_2:
    left, right = 0,n-1
    isExist = False
    while left <= right:
        mid = (left+right)//2
        if num == arr_1[mid]:
            isExist=True
            print(1)
            break
        elif num>arr_1[mid]:
            left = mid+1
        else:
            right = mid-1
    if not isExist:
        print(0)