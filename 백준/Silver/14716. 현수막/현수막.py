import sys
sys.setrecursionlimit(3000000)

m,n =map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
d = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]
cnt = 0

def dfs(i,j):
    arr[i][j] = 0 
    for dx, dy in d:
        x,y = dx+i, dy+j
        if 0<=x<m and 0<=y<n and arr[x][y]==1:
            dfs(x,y)

for i in range(m):
    for j in range(n):
        if arr[i][j]==1:
            dfs(i,j)
            cnt+=1
print(cnt)