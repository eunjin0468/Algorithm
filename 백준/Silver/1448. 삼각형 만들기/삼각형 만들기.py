import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort(reverse=True)
result = -1
for i in range(len(arr)-2):
    if arr[i] < arr[i+1]+arr[i+2]:
        result = arr[i]+arr[i+1]+arr[i+2]
        break
print(result)