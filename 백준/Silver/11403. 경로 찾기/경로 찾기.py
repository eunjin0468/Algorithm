n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

def dfs(i):
    for j in range(n):
        if arr[i][j]==1 and visited[j]==0:
            visited[j]=1
            dfs(j)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j]==1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n)]