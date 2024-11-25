n = int(input())
result = 0 
arr = [int(input()) for _ in range(n)]
for i in range(n-1, 0, -1):
    if arr[i]<=arr[i-1]:
        result += (arr[i-1]-arr[i])+1
        arr[i-1] = arr[i]-1
        
print(result)