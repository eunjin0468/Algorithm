import sys
sys.setrecursionlimit(10 ** 8)
n,m,k = map(int, input().split())
arr = [['.']*m for _ in range(n)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]
visited = [[0]*m for _ in range(n)]
res = []
def dfs(y,x):
    global cnt
    for k in range(4):
        Y,X = y+dy[k], x+dx[k]
        if 0<=Y<n and 0<=X<m and visited[Y][X]==0 and arr[Y][X]=='#':
            cnt+=1
            visited[Y][X]=1
            dfs(Y,X)
            
for _ in range(k):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    arr[a][b] = '#'
for i in range(n):
    for j in range(m):
        if arr[i][j]=='#' and visited[i][j]==0:
            visited[i][j]=1
            cnt=1
            dfs(i,j)
            res.append(cnt)
print(max(res))