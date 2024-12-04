n = int(input())
arr = [input().split() for _ in range(n)]
arr.sort()
print(max(arr, key=arr.count)[0])