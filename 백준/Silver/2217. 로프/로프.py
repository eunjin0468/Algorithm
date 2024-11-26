n = int(input())
arr = [int(input()) for _ in range(n)]
result = []
arr.sort(reverse=True)
for i in range(n):
    result.append(arr[i]*(i+1))
print(max(result))