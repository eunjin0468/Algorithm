import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
arr = [list(input()) for _ in range(n)]
res = []
visited = [[0]*n for _ in range(n)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]

def dfs(y,x):
    global cnt
    cnt+=1
    visited[y][x]=1
    for k in range(4):
        Y,X = y+dy[k], x+dx[k]
        if 0<=Y<n and 0<=X<n and visited[Y][X]==0 and arr[Y][X]=='1':
            dfs(Y,X)
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and visited[i][j]==0:
            cnt = 0
            dfs(i,j)
            res.append(cnt)
print(len(res))
res.sort(reverse=False)
print('\n'.join(map(str, res)))