import sys
input = sys.stdin.readline

def dfs(m,arr):
    arr[m]=-2
    for i in range(len(arr)):
        if m == arr[i]:
            dfs(i,arr)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = 0
dfs(m,arr)

for i in range(len(arr)):
    if arr[i]!=-2 and i not in arr:
        cnt+=1
print(cnt)