n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr1 = sorted(arr, key=lambda x:x[0])
arr2 = sorted(arr, key=lambda x:x[1])
x = arr1[-1][0] - arr1[0][0]
y = arr2[-1][1] - arr2[0][1]
print(x*y)