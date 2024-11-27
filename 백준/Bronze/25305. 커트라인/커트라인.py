a,b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr[b-1])